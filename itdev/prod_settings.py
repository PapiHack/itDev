from .settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['itdev.herokuapp.com']