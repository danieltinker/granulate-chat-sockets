from pymongo import MongoClient
import pymongo
from pymongo.errors import PyMongoError
try:
    client = MongoClient('localhost', 27017)
    print(client.server_info())
    print("connected")
except PyMongoError:
    print("server couldnt connect to db")
    
db = client['chatDB']


        
    


