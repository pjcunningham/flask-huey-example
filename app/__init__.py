# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

import os
from flask import Flask
from .views import HomeView


def create_app():
    _app = Flask('app')
    _app.config.from_object(os.environ['APP_SETTINGS'])

    from .extensions import configure_extensions
    configure_extensions(_app)

    _app.add_url_rule('/', view_func=HomeView.as_view('home'))

    return _app


def create_huey_app():
    _app = Flask('huey-app')
    _app.config.from_object(os.environ['HUEY_APP_SETTINGS'])

    from .extensions import configure_extensions
    configure_extensions(_app)

    return _app
