"""
This Module is for Grabing simple data from tba without filling up the database server!
"""

import tbapy as tba
import yaml
import json 
import sys
import logging

sys.path.append("src/flask")
logging.basicConfig(filename='flask.log',level=logging.DEBUG)

with open(r'src/config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    
    
tba = tba.TBA(config["API_KEY"])
status = tba.status()

json_status = json.dumps(status)
deserial_json =json.loads(json_status)

def getCurrentyear():
    logging.info("got year ")
    return deserial_json['current_season']

def getApistatus():
    logging.info("got api Status is")
    return 