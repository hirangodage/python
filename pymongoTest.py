from pymongo import MongoClient
import json

f=open("credentials.json",'r')
y = json.loads(f.read())

client = MongoClient(y["mongoconnection"])
db = client.sample_weatherdata
collection = db.data
print(collection.find_one({'elevation': 9999}))