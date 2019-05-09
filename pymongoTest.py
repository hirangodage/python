from pymongo import MongoClient
import json
from collections import namedtuple
# get secrets from json file. its not there in repo
f=open("credentials.json",'r')
y = json.loads(f.read())

client = MongoClient(y["mongoconnection"])
db = client.sample_weatherdata
collection = db.data
print(collection.find_one({'elevation': 9999})['precipitationEstimatedObservation']["estimatedWaterDepth"])