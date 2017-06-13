# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

from . import (
    mail
)


def configure_extensions(app):

    mail.configure(app)

    if app.config.get('DEBUG_TOOLBAR_ENABLED'):
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            DebugToolbarExtension(app)
        except:
            pass

