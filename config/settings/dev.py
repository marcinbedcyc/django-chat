from .base import *  # noqa
from .base import env

DEBUG = True
SECRET_KEY = env('DJANGO_SECRET_KEY', default='!!!SET DJANGO SECRET KEY!!!')

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

INSTALLED_APPS += ['debug_toolbar', 'django_extensions',]  # noqa

# * The order of MIDDLEWARE is important. You should include the Debug
# * Toolbar middleware as early as possible in the list. However, it must come
# * after any other middleware that encodes the response’s content, such as GZipMiddleware.
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa

# Console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Works with Docker
if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(env('REDIS_URL'), env('REDIS_PORT'))]
        }
    }
}
