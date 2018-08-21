# config.py
from huey import RedisHuey
from app.config import ProductionConfig

# huey = RedisHuey()
# huey = RedisHuey('my-queue', url='http://localhost:6379')
huey = RedisHuey('my-queue', url=ProductionConfig.REDIS_URL)
