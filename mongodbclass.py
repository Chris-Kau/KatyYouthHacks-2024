from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
mongodbui = os.getenv("PYMONGOUURI")
client = MongoClient(mongodbui, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#db = client.CalendarAI
db = client.sample_mflix

def list_collection():
    return db.collection.find()
    
def find_collection(searched_collection):
    collection = db.list_collection_names()
    for name in collection:
        if name == searched_collection:
            return db[name]
    return None

def list_collection_documents(collection):
    if collection == None:
        return
    temp = []
    for doc in collection.find():
        temp.append(doc)
    return temp

def get_doc(collection, searched_doc):
    for doc in collection.find():
        if doc["_id"] == searched_doc:



list_collection_documents(find_collection("sessions"))