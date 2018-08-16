# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

import os
from flask import Flask
from .views import Example1View
from app import config


# basedir = os.path.abspath(os.path.dirname(__file__))
#
# if os.path.exists('config.env'):
#     print('Importing environment from .env file')
#     for line in open('config.env'):
#         var = line.strip().split('=')
#         if len(var) == 2:
#             os.environ[var[0]] = var[1].replace("\"", "")

# https://damyanon.net/post/flask-series-configuration/

def create_app():
    _app = Flask('app')
    _app.config.from_object(os.environ['APP_SETTINGS'])
    # _app.config.from_object(config.DevelopmentConfig)
    print('in init/create_app')

    from .extensions import configure_extensions
    configure_extensions(_app)

    _app.add_url_rule('/', view_func=Example1View.as_view('home'))

    return _app


def create_huey_app():
    _app = Flask('huey-app')
    # _app.config.from_object(os.environ['APP_SETTINGS'])
    _app.config.from_object(os.environ['HUEY_APP_SETTINGS'])

    from .extensions import configure_extensions
    configure_extensions(_app)

    return _app

