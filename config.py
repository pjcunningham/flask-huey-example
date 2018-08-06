# config.py
from huey import RedisHuey

huey = RedisHuey()
# huey = RedisHuey('my-queue', url='http://localhost:6379')