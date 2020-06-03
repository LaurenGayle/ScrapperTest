"""
This module is for handling the actual scraping of the json data. this data will eventually end up on the sql database
"""

import requests
import database
import tbapy as tba


tba = tba.TBA(database.config["API_KEY"])
status = tba.status()

# Uses Config.yml to get relevent info like Json Api url to pull data 
def startRequest():
    try:
       database.logging.debug("Connecting to tba")  
       #print(tba.status())
       #pushes tba status to mongo
       database.monoPush(status)
       
    except:
        database.logging.critical("TBA OFFLINE")
