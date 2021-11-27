from datetime import time
from typing import Collection
from flask.json import jsonify
from connectionDB import db
import time

class MessageCollection():
    messageCollection = db.get_collection('messages')     
    
    def set(self,roomname,username):
        self.messageCollection.insert_one({
            "roomname":roomname,
            "name":username,
            "text":str(time.time()) + ": " + username + "joined to Room: " + roomname,
            "timestamp":time.time()
            })
        return jsonify({'isOk':True})
    
    def insertMsg(self,roomname,username,msg):
        msgObj = self.messageCollection.find({'roomname':roomname})
        self.messageCollection.insert_one({
            'roomname':roomname,
            "username":username,
            "text":msg,
            "timestamp":time.time()
        })
        return jsonify({'msg':msg})
        
    def getChat(self,roomID):
        index=0
        msgs = self.messageCollection.find({'roomname':roomID})
        msgArr=[]
        for msg in msgs:
            index+=1
            msgArr.append(msg["username"] + ": " + msg["text"])
        if(index==0):
            return{'empty':'empty'},204
        return jsonify({'msgs':msgArr}) 