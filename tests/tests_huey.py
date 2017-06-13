# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

import os
import unittest
from app.extensions.queue import create_huey
import redis

TEST_POOL = redis.ConnectionPool(host='10.0.0.1', port=6379, db=0)
REDIS_URL = 'redis://[:password]@localhost:9000/1'
UNIX_URL = 'unix://[:password]@/path/to/socket.sock?db=2'

_config_1 = dict(
    HUEY_STORAGE_READ_TIMEOUT=1,
    HUEY_STORAGE_MAX_ERRORS=1,
    HUEY_STORAGE_CONNECTION_POOL=TEST_POOL,

    HUEY_TASK_QUEUE_NAME='THIS-IS-A-TEST',
    HUEY_RESULT_STORE=False,
    HUEY_EVENTS=False,
    HUEY_STORE_NONE=False,
    HUEY_ALWAYS_EAGER=False,
    HUEY_STORE_ERRORS=False,
    HUEY_BLOCKING=False
)

_config_2 = dict(
    HUEY_STORAGE_READ_TIMEOUT=1,
    HUEY_STORAGE_MAX_ERRORS=1,
    HUEY_STORAGE_URL=REDIS_URL,

    HUEY_TASK_QUEUE_NAME='THIS-IS-A-TEST',
    HUEY_RESULT_STORE=False,
    HUEY_EVENTS=False,
    HUEY_STORE_NONE=False,
    HUEY_ALWAYS_EAGER=False,
    HUEY_STORE_ERRORS=False,
    HUEY_BLOCKING=False
)

_config_3 = dict(
    HUEY_STORAGE_READ_TIMEOUT=1,
    HUEY_STORAGE_MAX_ERRORS=1,
    HUEY_STORAGE_URL=UNIX_URL,

    HUEY_TASK_QUEUE_NAME='THIS-IS-A-TEST',
    HUEY_RESULT_STORE=False,
    HUEY_EVENTS=False,
    HUEY_STORE_NONE=False,
    HUEY_ALWAYS_EAGER=False,
    HUEY_STORE_ERRORS=False,
    HUEY_BLOCKING=False
)


class ConfigMixin(object):

    def test_name(self):
        self.assertEqual(self.huey.name, 'THIS-IS-A-TEST')

    def test_result_store(self):
        self.assertEqual(self.huey.result_store, False)

    def test_events(self):
        self.assertEqual(self.huey.events, False)

    def test_store_none(self):
        self.assertEqual(self.huey.store_none, False)

    def test_always_eager(self):
        self.assertEqual(self.huey.always_eager, False)

    def test_store_errors(self):
        self.assertEqual(self.huey.store_errors, False)

    def test_blocking(self):
        self.assertEqual(self.huey.blocking, False)

    def test_storage_read_timeout(self):
        self.assertEqual(self.huey.storage.read_timeout, 1)

    def test_storage_max_errors(self):
        self.assertEqual(self.huey.storage.max_errors, 1)


class HueyConfig1Tests(unittest.TestCase, ConfigMixin):

    def setUp(self):
        self.huey = create_huey(_config_1)

    def test_storage_connection_pool_host(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['host'], '10.0.0.1')

    def test_storage_connection_pool_port(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['port'], 6379)

    def test_storage_connection_pool_db(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['db'], 0)


class HueyConfig2Tests(unittest.TestCase, ConfigMixin):
    def setUp(self):
        self.huey = create_huey(_config_2)

    def test_storage_connection_pool_host(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['host'], 'localhost')

    def test_storage_connection_pool_password(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['password'], 'password')

    def test_storage_connection_pool_port(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['port'], 9000)

    def test_storage_connection_pool_db(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['db'], 1)


class HueyConfig2Tests(unittest.TestCase, ConfigMixin):
    def setUp(self):
        self.huey = create_huey(_config_3)

    def test_storage_connection_pool_host(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['path'], '/path/to/socket.sock')

    def test_storage_connection_pool_password(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['password'], 'password')

    def test_storage_connection_pool_db(self):
        self.assertEqual(self.huey.storage.pool.connection_kwargs['db'], 2)


if __name__ == "__main__":
    unittest.main()
