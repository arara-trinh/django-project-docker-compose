from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'db',
        'PORT': '3306',    
    }
}