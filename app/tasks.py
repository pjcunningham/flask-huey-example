# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

from huey import crontab
from app import create_huey_app
from huey_config import config
from app.extensions.queue import create_huey
from app.extensions.mail import mail

huey = create_huey(config)

@huey.task()
def send_async_email(msg):
    """Background task to send an email with Flask-Mail."""
    app = create_huey_app()
    with app.app_context():
        mail.send(msg)