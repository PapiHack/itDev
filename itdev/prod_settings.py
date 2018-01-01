from .settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = 'e+@i0%kr6ku^o&&$#t=yi0$$s=(4spi9(hak46*fwjqv*jc0+v'

ALLOWED_HOSTS = ['itdev.herokuapp.com']