from flask import Flask,request,jsonify
from flask.templating import render_template
from flask_restful import Api,Resource,reqparse
from handlers.messageHandler import MessageCollection
from handlers.roomHandler import RoomCollection

room_put_args = reqparse.RequestParser()
room_put_args.add_argument("name", type=str)
msg_put_args = reqparse.RequestParser()
msg_put_args.add_argument("roomname", type=str)
msg_put_args.add_argument("name", type=str)
msg_put_args.add_argument("msg", type=str)
msg_get_args = reqparse.RequestParser()
msg_get_args.add_argument("roomname",type=str)

app = Flask(__name__)
api =  Api(app)

class Room(Resource):
    def get(self):
        pass

    def put(self,roomname):
        args = room_put_args.parse_args()
        RoomCollection().set(roomname,args['name'])
        return{roomname:args}

api.add_resource(Room, "/room/<string:roomname>")

class Message(Resource):
    def get(self):
        args = msg_get_args.parse_args()
        return MessageCollection().getChat(args['roomname'])
    def post(self):
        pass      
    def put(self):
        args = msg_put_args.parse_args()
        return MessageCollection().insertMsg(args['roomname'],args['name'],args['msg']+"\n")

api.add_resource(Message, "/message")

@app.route("/isON", methods=['GET'])
def isOn():
    return jsonify({'ok':'ok'})

if __name__ == "__main__":
    app.run(debug=True)