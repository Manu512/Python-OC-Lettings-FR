"""
Production Settings for Heroku
"""
# flake8: noqa: F403 , F405 # Bypass Flake8 star import
# If using in your own project, update the project namespace below
from .base import *

# False if not in os.environ
DEBUG = False

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
