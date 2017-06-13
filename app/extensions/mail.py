# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

from flask_mail import Mail
mail = Mail()

def configure(app):
    mail.init_app(app)