from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import *
import os
from dotenv import load_dotenv, dotenv_values
from datetime import datetime

load_dotenv()
mongodbui = os.getenv("PYMONGOUURI")
# client = MongoClient(mongodbui, server_api=ServerApi('1'))
client = connect(db="CalendarAI", host=mongodbui)
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

#db = client.CalendarAI
db = client.sample_mflix

# def list_collection():
#     return db.collection.find()
    
# def find_collection(searched_collection):
#     collection = db.list_collection_names()
#     for name in collection:
#         if name == searched_collection:
#             return db[name]
#     return None

# def list_collection_documents(collection):
#     if collection == None:
#         return
#     temp = []
#     for doc in collection.find():
#         temp.append(doc)
#     return temp

# def get_doc(collection, searched_doc):
#     for doc in collection.find():
#         if doc["_id"] == searched_doc:
#             pass


# list_collection_documents(find_collection("sessions"))

class DBEvent(EmbeddedDocument):
    name = StringField(db_field="name", required=True)
    description = StringField(db_field="description", max_length=50)
    hour = IntField(db_field="hour", required=True, min_value=0, max_value=23)
    minute= IntField(db_field="minute", required=True, min_value=0, max_value=59)

    def __init__(self, name, description, hour, minute, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"name: {self.name}; description: {self.description}; time: {self.hour}:{self.minute}"


class DBDay(Document):
    calendar_date = DateTimeField(db_field='calendar_date', required=True)
    events = EmbeddedDocumentListField(DBEvent, db_field='events')

    meta = {'collection': 'days',
            'indexes': [
                {'unique': True, 'fields': ['calendar_date'], 'name': 'days_pk_01'},
            ]}

    def __init__(self, calendar_date, *args, **values):
        super().__init__(*args, **values)
        self.calendar_date = calendar_date

    def add_event(self, new_event):
        print("hoola hoops")
        if not self.events:
            self.events = [new_event]
            return
        
        self.events.append(new_event)
        self.save()
    
    def __str__(self):
        return f"date: {self.calendar_date}\n"


def list_days():
    for day in DBDay.objects:
        print(day)


def find_days(date):
    for day in DBDay.objects:
        if day['calendar_date'] == date:
            return day
    return None



