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

# Absolute paths for where the project and templates are stored.
ABSOLUTE_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
RELATIVE_PROJECT_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, '../'))
ABSOLUTE_TEMPLATES_PATH = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'templates/'))
ABSOLUTE_STATICFILES_PATH = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'staticfiles/'))
ABSOLUTE_SWEETALERTS_TEMPLATES_PATH = os.path.abspath(os.path.join(RELATIVE_PROJECT_ROOT, 'templates/'))

TEMPLATE_DIRS = (
    ABSOLUTE_TEMPLATES_PATH,
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b-g(rm-rwiz^szsv!i+=_8eiq^)oc5*s$=lx@f8575am-672n_'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gifsong',

    'south',
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

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    ABSOLUTE_STATICFILES_PATH,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


if(HEROKU):
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    try:
        if(os.environ['DJANGO_SECRET']):
            # Secret Key
            SECRET_KEY = os.environ['DJANGO_SECRET']
    except:
        pass

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Static asset configuration
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'static/'
    STATIC_URL = 'https://googledrive.com/host/0B30fK9bxmUN5QnRlN0VpVEgyYUk/'

    STATICFILES_DIRS = (
           os.path.join(BASE_DIR, 'staticfiles'),
    )
