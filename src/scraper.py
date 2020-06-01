"""
This module is for handling the actual scraping of the json data. this data will eventually end up on the sql database
"""

import requests
import database
from requests.exceptions import HTTPError


# Uses Config.yml to get relevent info like Json Api url to pull data 
def startRequest():
    try:
        response = requests.get(database.config["API_URL"])