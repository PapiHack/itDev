from .settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['itworker.herokuapp.com']