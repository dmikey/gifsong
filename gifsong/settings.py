"""
Django settings for gifsong project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

# Debugging and deployment things.
# Add NOTHEROKU='true' to your environment vars
LOCALDEV = False
HEROKU = True
try:
    if(os.environ['NOTHEROKU']):
        LOCALDEV = True
        HEROKU = False
except:
    pass
TEMPLATE_DEBUG = DEBUG = LOCALDEV

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b-g(rm-rwiz^szsv!i+=_8eiq^)oc5*s$=lx@f8575am-672n_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gifsong.urls'

WSGI_APPLICATION = 'gifsong.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


if(HEROKU):
    # Parse database configuration from $DATABASE_URL
    if(DEBUG != True):
        import dj_database_url
        DATABASES['default'] =  dj_database_url.config()
        # Allow all host headers
        ALLOWED_HOSTS = ['*']
    
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Static asset configuration
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'sweeterp/static/'
    STATIC_URL = '/static/'
    
    STATICFILES_DIRS = (
           os.path.join(BASE_DIR, 'staticfiles'),
    )