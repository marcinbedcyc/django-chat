from .base import *  # noqa
from .base import env

SECRET_KEY = env('DJANGO_SECRET_KEY')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(env('REDIS_URL'), env('REDIS_PORT'))]
        }
    }
}
