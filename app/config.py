# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

import os


class Config(object):
    SECRET_KEY = 'b2ac76038b0958772c7981da84de0f43b4962721cd51fe09'

    DEBUG_TOOLBAR_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    MAIL_DEFAULT_SENDER = 'paul@localhost'
    # REDIS_URL = os.getenv('REDISTOGO_URL') or 'http://localhost:6379'



class ProductionConfig(Config):
    REDIS_URL = os.getenv('REDISTOGO_URL') or 'http://localhost:6379'
    print('PROCUTION CONFIG')
    print(REDIS_URL)
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TOOLBAR_ENABLED = True


class StagingConfig(Config):
    pass


class TestingConfig(Config):
    pass