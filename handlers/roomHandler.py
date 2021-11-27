from typing import Collection

from flask.json import jsonify
from connectionDB import db

class RoomCollection():
    roomCollection = db.get_collection('rooms')     
    msgCollection = db.get_collection('messages')
      
    def set(self, roomname,user):
        self.roomCollection.insert_one({
            'roomname':roomname,
            'name':user
            })
        return jsonify({'roomname':roomname})
        
    def userJoin(self,roomname,user):
        myroom = self.roomCollection.find_one({"roomname":roomname})
        self.roomCollection.update_one({"_id":myroom["_id"]},
                                        {"$push":{'users':user}})
        
        return jsonify({'user':user})
    
    def getChat(self,roomID):
        msgs = self.msgCollection.find({'roomname':roomID})
        return jsonify({'msgs':msgs})
        
    def read(self):
        pass
        
    def update(self):
        pass
    
    def delete(self):
        pass