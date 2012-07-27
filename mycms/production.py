from settings import *

import json

with open('/app/conf/environment.json') as f:
    env = json.load(f)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': env['DB_NAME'],
          'USER': env['DB_USER'],
          'PASSWORD': env['DB_PASSWORD'],
          'HOST': env['DB_HOST'],
          'PORT': env['DB_PORT'],
        }
    }
