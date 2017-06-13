# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

from app import create_app

if __name__ == '__main__':

    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    app = create_app()
    app.run(host='localhost', port=6060, debug=True)
