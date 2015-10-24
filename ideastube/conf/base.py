# -*- coding: utf-8 -*-
"""Django settings for ideastube project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import subprocess

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'ideastube')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '16exrv_@=2(za=oj$tj+l_^v#sbt83!=t#wz$s+1udfa04#vz!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', True))

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.ideasbox.lan.', 'localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ideastube',
    'ideastube.serveradmin',
    'ideastube.blog',
    'ideastube.library',
    'ideastube.search',
    'ideastube.mediacenter',
    'ideastube.monitoring',
    'taggit',
    'django_countries',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "ideastube.context_processors.settings",
    "ideastube.context_processors.version",
)

ROOT_URLCONF = 'ideastube.urls'

WSGI_APPLICATION = 'ideastube.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

AVAILABLE_LANGUAGES = (
    ('en', 'English'),
    ('fr', u'Français'),
    ('ar', u'العربية'),
)

SUPPORTED_LANGUAGES = os.environ.get('SUPPORTED_LANGUAGES', 'fr en ar').split()
LANGUAGES = []
for code, label in AVAILABLE_LANGUAGES:
    if code in SUPPORTED_LANGUAGES:
        LANGUAGES.append((code, label))

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'ideastube', 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# Ideas Box specifics
STORAGE_ROOT = os.environ.get('STORAGE_ROOT',
                              os.path.join(BASE_DIR, 'storage'))

BACKUPED_ROOT = os.path.join(STORAGE_ROOT, 'main')

MEDIA_ROOT = os.path.join(BACKUPED_ROOT, 'media')
STATIC_ROOT = os.path.join(STORAGE_ROOT, 'static')

AUTH_USER_MODEL = 'ideastube.User'
IDEASTUBE_NAME = 'debugbox'
IDEASTUBE_PLACE_NAME = _('the camp')
IDEASTUBE_BODY_ID = 'ideasbox'

LOAN_DURATION = 0  # In days.

DOMAIN = 'ideasbox.lan'
WIKIPEDIA_URL = 'http://wikipedia.{domain}'.format(domain=DOMAIN)
KHANACADEMY_URL = 'http://khanacademy.{domain}'.format(domain=DOMAIN)

# Fields to be used in the entry export. This export is supposed to be
# anonymized, so no personal data like name.
MONITORING_ENTRY_EXPORT_FIELDS = ['birth_year', 'gender']

USERS_LIST_EXTRA_FIELDS = ['serial']

USER_INDEX_FIELDS = ['short_name', 'full_name', 'serial']

USER_FORM_FIELDS = (
    (_('Basic informations'), ['serial', 'short_name', 'full_name']),
    (_('Language skills'), ['ar_level', 'en_level']),
)

ENTRY_ACTIVITY_CHOICES = [
]

STAFF_HOME_CARDS = [
    {
        'is_staff': True,
        'category': 'manage',
        'url': 'user_list',
        'title': _('Users'),
        'description': _('Create, remove or modify users.'),
        'fa': 'users',
    },
    {
        'is_staff': True,
        'category': 'manage',
        'url': 'monitoring:entry',
        'title': _('Entries'),
        'description': _('Manage user entries.'),
        'fa': 'sign-in',
    },
    {
        'is_staff': True,
        'category': 'manage',
        'url': 'monitoring:stock',
        'title': _('Stock'),
        'description': _('Manage stock.'),
        'fa': 'barcode',
    },
    {
        'is_staff': True,
        'category': 'manage',
        'url': 'monitoring:loan',
        'title': _('Loans'),
        'description': _('Manage loans.'),
        'fa': 'exchange',
    },
    {
        'is_staff': True,
        'category': 'manage',
        'url': 'server:power',
        'title': _('Stop/Restart'),
        'description': _('Stop or restart the server.'),
        'fa': 'power-off',
    },
    {
        'is_staff': True,
        'category': 'manage',
        'url': 'server:backup',
        'title': _('Backups'),
        'description': _('Create, restore, download, upload backups.'),
        'fa': 'life-ring',
    },
]

HOME_CARDS = STAFF_HOME_CARDS + [
    {
        'id': 'blog',
    },
    {
        'id': 'library',
    },
    {
        'id': 'mediacenter',
    },
    {
        'id': 'wikipedia',
    },
    {
        'id': 'khanacademy',
    },
    # {
    #     'category': 'learn',
    #     'url': 'http://mydomain.fr',
    #     'title': 'The title of my custom card',
    #     'description': 'The description of my custom card',
    #     'img': '/img/wikipedia.png',
    #     'fa': 'fax',
    # },
]

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BACKUPED_ROOT, 'default.sqlite'),
    }
}

SERVICES = [
    {'name': 'ideastube', 'description': _('Ideastube web server')},
    {'name': 'nginx', 'description': _('Global proxy')},
    {
        'name': 'kalite',
        'description': _('Daemon which provides KhanAcademy on lan'),
        'status_caller': lambda x: {'status': False} if subprocess.call(['pgrep', 'kalite', '-f']) else {'status': True}  # noqa
    },
    {'name': 'kiwix',
        'description': _('Daemon which provides Wikipedia on lan')},
    {'name': 'ntp', 'description': _('Net time protocol')},
    {'name': 'ssh',
        'description': _('Daemon used for distant connexion to server')},
]


SESSION_COOKIE_AGE = 60 * 60  # Members must be logged out after one hour
BACKUP_FORMAT = 'zip'  # One of 'zip', 'tar', 'bztar', 'gztar'