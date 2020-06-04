# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask_migrate import Migrate
from os import environ
from sys import exit
import sys
from config import config_dict
from app import create_app, db
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
get_config_mode = environ.get('APPSEED_CONFIG_MODE', 'Debug')

sys.path.append("src/")
try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid APPSEED_CONFIG_MODE environment variable entry.')

app = create_app(config_mode)
mongo = MongoClient("mongodb://50.116.37.86:27017/") 

Migrate(app, db)

if __name__ == "__main__":
    app.run()
