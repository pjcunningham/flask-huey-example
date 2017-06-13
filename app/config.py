# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'


class Config(object):
    SECRET_KEY = 'b2ac76038b0958772c7981da84de0f43b4962721cd51fe09'

    DEBUG_TOOLBAR_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    MAIL_DEFAULT_SENDER = 'paul@localhost'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TOOLBAR_ENABLED = True


class StagingConfig(Config):
    pass


class TestingConfig(Config):
    pass