"""
This Module is For Connecting My Mongodb server to python for dumping scraped data to

"""
import os
import yaml
import logging
from pymongo import MongoClient
from bson.objectid import ObjectId


logging.basicConfig(filename='example.log',level=logging.DEBUG)

with open(r'config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    
client = MongoClient("mongodb://50.116.37.86:27017/")
db = client['Data']
collection = db['test']




# This will test connection to database server and log the stages of connection to database 
def mongoConnect():
    logging.debug("Connecting to Mongodb!")
    try:
        logging.info(client.server_info())
    except:
        logging.critical("CANNOT CONNECT TO MONGODB")
        
# THis will push data in json format from tba to Mongo    
def monoPush(tbadata):
    logging.debug("Adding data to db")
    
    data = collection.insert_one(tbadata).inserted_id
    data
   
   
    

def getFRCyear():
   return

