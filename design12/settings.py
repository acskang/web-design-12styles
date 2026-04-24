import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_SECRET_KEY = 'django-insecure-yordug50p8&e&zqmm9%_r5)y!@zj8kr(5p@9sr#t5p3@=9#aju'


def _csv_env(name, default):
    return [
        item.strip()
        for item in os.environ.get(name, default).split(',')
        if item.strip()
    ]


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', DEFAULT_SECRET_KEY)
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'

if not DEBUG and SECRET_KEY == DEFAULT_SECRET_KEY:
    raise RuntimeError('DJANGO_SECRET_KEY must be set when DJANGO_DEBUG=0')

default_allowed_hosts = [
    '127.0.0.1',
    'localhost',
    'webdesign.thesysm.com',
]
ALLOWED_HOSTS = _csv_env('DJANGO_ALLOWED_HOSTS', ','.join(default_allowed_hosts))

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'showroom',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'design12.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'design12.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(os.environ.get('DJANGO_SQLITE_PATH', BASE_DIR / 'db.sqlite3')),
    }
}

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('ko', 'Korean'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True
USE_TZ = True
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': (
            'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
            if not DEBUG
            else 'django.contrib.staticfiles.storage.StaticFilesStorage'
        ),
    },
}

CSRF_TRUSTED_ORIGINS = _csv_env(
    'DJANGO_CSRF_TRUSTED_ORIGINS',
    'https://webdesign.thesysm.com',
)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = os.environ.get('DJANGO_SECURE_SSL_REDIRECT', '0') == '1'
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
X_FRAME_OPTIONS = 'DENY'

if not DEBUG:
    SECURE_HSTS_SECONDS = int(os.environ.get('DJANGO_SECURE_HSTS_SECONDS', '86400'))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get(
        'DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS',
        '1',
    ) == '1'
    SECURE_HSTS_PRELOAD = os.environ.get('DJANGO_SECURE_HSTS_PRELOAD', '0') == '1'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
