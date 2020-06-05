# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

import pymongo
import run
import tbadata
import json
import datetime
import random
import time
from httplib2 import Response


data = run.mongo['Data']
col = data['test']

current_year = tbadata.getCurrentyear()

#IN SERTED DATA TO FLASK
@blueprint.route('/index')
def index():
    return render_template('index2.html',year=current_year,random = chart_data)

@blueprint.route('/<template>')
def route_template(template):
    try:

        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500
