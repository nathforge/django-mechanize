import os.path
import sys

DEBUG = True

SITE_ROOT = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(SITE_ROOT, '..'))

MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'temp', 'testdb.sqlite'),
    },
}

INSTALLED_APPS = (
    'testapp',
)
