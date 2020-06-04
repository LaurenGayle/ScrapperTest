# -*- encoding: utf-8 -*-
"""
This is the Main module
starting Call Main Project functions here Ie Starting program
"""

from flask import Blueprint

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)
