from .base import *  # noqa

DEBUG = True
SECRET_KEY = 'django-insecure-7)wwmlw(a0qon)8@cx(+o3dtk7gq5n4&ttnyty5!dlr#u=-m4l'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT_DIR / 'db.sqlite3',  # noqa
        # Tweak for Channels live server
        # https://channels.readthedocs.io/en/stable/topics/testing.html#channelsliveservertestcase
        'TEST': {
            'NAME': ROOT_DIR / 'db_test.sqlite3'  # noqa
        }
    }
}

CELERY_TASK_ALWAYS_EAGER = True

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
