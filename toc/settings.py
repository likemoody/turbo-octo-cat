"""
Django settings for toc project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from sensitive import env_vars

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.path.join(BASE_DIR, '../../sensitive/env_vars.py')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOCAL = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
    'postmydreams.herokuapp.com/',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 1
}

PROJECT_VERSION = 'alpha 0.3'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_blog.apps.AppBlogConfig',
    'app_users.apps.AppUsersConfig',
    'app_bookcrossing.apps.AppBookcrossingConfig',
    'crispy_forms',
    'rest_framework',
    'django_telegrambot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'toc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'app_blog/templates/app_blog'),
            os.path.join(BASE_DIR, 'app_users/templates/app_users'),
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'toc.context_processors.project_general',
                'toc.context_processors.unread_messages',
            ],
        },
    },
]
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
)

WSGI_APPLICATION = 'toc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if LOCAL:
    DATABASES = {
        'default': {
            'HOST': '127.0.0.1',
            'NAME': env_vars.DB_NAME,
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': env_vars.DB_LOGIN,
            'PASSWORD': env_vars.DB_PASS,
        }
    }
else:
    DATABASES = {
        'default': {
            'HOST': os.environ.get("DB_HOST_PMD"),
            'NAME': os.environ.get("DB_NAME_PMD"),
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': os.environ.get("DB_LOGIN_PMD"),
            'PASSWORD': os.environ.get("DB_PASS_PMD"),
            'PORT': os.environ.get("DB_PORT_PMD"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# settings.py
# Django Telegram Bot settings

DJANGO_TELEGRAMBOT = {

    'MODE': 'WEBHOOK',  # (Optional [str]) # The default value is WEBHOOK,
    # otherwise you may use 'POLLING'
    # NB: if use polling you must provide to run
    # a management command that starts a worker

    # 'WEBHOOK_SITE': 'https://mywebsite.com',
    'WEBHOOK_SITE': 'https://postmydreams.herokuapp.com/',
    'WEBHOOK_PREFIX': '/prefix',  # (Optional[str]) # If this value is specified,
    # a prefix is added to webhook url

    # 'WEBHOOK_CERTIFICATE' : 'cert.pem', # If your site use self-signed
    # certificate, must be set with location of your public key
    # certificate.(More info at https://core.telegram.org/bots/self-signed )

    'STRICT_INIT': True,  # If set to True, the server will fail to start if some of the
    # apps contain telegrambot.py files that cannot be successfully
    # imported.

    'BOTS': [
        {
            'TOKEN': os.environ.get('JM_TEST_BOT_TOKEN'),  # Your bot token.

            # 'ALLOWED_UPDATES':(Optional[list[str]]), # List the types of
            # updates you want your bot to receive. For example, specify
            # ``["message", "edited_channel_post", "callback_query"]`` to
            # only receive updates of these types. See ``telegram.Update``
            # for a complete list of available update types.
            # Specify an empty list to receive all updates regardless of type
            # (default). If not specified, the previous setting will be used.
            # Please note that this parameter doesn't affect updates created
            # before the call to the setWebhook, so unwanted updates may be
            # received for a short period of time.

            # 'TIMEOUT':(Optional[int|float]), # If this value is specified,
            # use it as the read timeout from the server

            # 'WEBHOOK_MAX_CONNECTIONS':(Optional[int]), # Maximum allowed number of
            # simultaneous HTTPS connections to the webhook for update
            # delivery, 1-100. Defaults to 40. Use lower values to limit the
            # load on your bot's server, and higher values to increase your
            # bot's throughput.

            # 'MESSAGEQUEUE_ENABLED':(Optinal[bool]), # Make this True if you want to use messagequeue

            # 'MESSAGEQUEUE_ALL_BURST_LIMIT':(Optional[int]), # If not provided 29 is the default value

            # 'MESSAGEQUEUE_ALL_TIME_LIMIT_MS':(Optional[int]), # If not provided 1024 is the default value

            # 'MESSAGEQUEUE_REQUEST_CON_POOL_SIZE':(Optional[int]), # If not provided 8 is the default value

            # 'POLL_INTERVAL' : (Optional[float]), # Time to wait between polling updates from Telegram in
            # seconds. Default is 0.0

            # 'POLL_CLEAN':(Optional[bool]), # Whether to clean any pending updates on Telegram servers before
            # actually starting to poll. Default is False.

            # 'POLL_BOOTSTRAP_RETRIES':(Optional[int]), # Whether the bootstrapping phase of the `Updater`
            # will retry on failures on the Telegram server.
            # |   < 0 - retry indefinitely
            # |     0 - no retries (default)
            # |   > 0 - retry up to X times

            # 'POLL_READ_LATENCY':(Optional[float|int]), # Grace time in seconds for receiving the reply from
            # server. Will be added to the `timeout` value and used as the read timeout from
            # server (Default: 2).
        },
        # Other bots here with same structure.
    ],

}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'pl-PL'

LANGUAGES = [
    ('pl', 'Polish'),
    ('en', 'English'),
    ('uk', 'Ukrainian'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/')
]

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'UTC'
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'blog-home'

import dj_database_url

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Activate Django-Heroku added at the bottom
django_heroku.settings(locals())
