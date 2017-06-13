# coding: utf-8

__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

from huey import RedisHuey

def create_huey(config):
    _storage_args = {
        'read_timeout': config.get('HUEY_STORAGE_READ_TIMEOUT', 1),
        'max_errors': config.get('HUEY_STORAGE_MAX_ERRORS', 1000),
        'connection_pool': config.get('HUEY_STORAGE_CONNECTION_POOL', None),
        'url': config.get('HUEY_STORAGE_URL', None),
    }

    _huey = RedisHuey(
        name=config.get('HUEY_TASK_QUEUE_NAME', 'FLASK-HUEY-EXAMPLE'),
        result_store=config.get('HUEY_RESULT_STORE', False),
        events=config.get('HUEY_EVENTS', True),
        store_none=config.get('HUEY_STORE_NONE', False),
        always_eager=config.get('HUEY_ALWAYS_EAGER', False),
        store_errors=config.get('HUEY_STORE_ERRORS', True),
        blocking=config.get('HUEY_BLOCKING', False),
        **_storage_args
    )
    return _huey

