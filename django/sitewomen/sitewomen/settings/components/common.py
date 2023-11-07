"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from typing import Dict, List, Tuple, Union

from django.utils.translation import gettext_lazy as _

from sitewomen.settings.components import BASE_DIR, config
# from settings.components import BASE_DIR, config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = config('DJANGO_SECRET_KEY')

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Your apps go here:
    'women.apps.WomenConfig',
    'users.apps.UsersConfig',

    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',


    # Security:


    # Health checks:
    # You may want to enable other checks as well,
    # see: https://github.com/KristianOellegaard/django-health-check

)

MIDDLEWARE: Tuple[str, ...] = (
    # Logging:
    # 'server.settings.components.logging.LoggingContextVarsMiddleware',

    # Content Security Policy:
    # 'csp.middleware.CSPMiddleware',

    # Django:
    'django.middleware.security.SecurityMiddleware',
    # django-permissions-policy
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Axes:
    # 'axes.middleware.AxesMiddleware',

    # Django HTTP Referrer Policy:
    # 'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
)

ROOT_URLCONF = 'sitewomen.urls'

# WSGI_APPLICATION = 'server.wsgi.application'
WSGI_APPLICATION = 'sitewomen.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD', cast=str),
        'HOST': config('DJANGO_DATABASE_HOST'),
        'PORT': config('DJANGO_DATABASE_PORT', cast=int),
        'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
        'OPTIONS': {
            'connect_timeout': 10,
            'options': '-c statement_timeout=15000ms',
        },
    },
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'  # 'en-us'

USE_I18N = True

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)

# LOCALE_PATHS = (
#     'locale/',
# )

USE_TZ = True
TIME_ZONE = 'UTC'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Список нестандартных путей к статическим файлам
STATICFILES_DIRS = (BASE_DIR / 'static',)

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )


# Templates
# https://docs.djangoproject.com/en/4.2/ref/templates/api

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Media files
# Media root dir is commonly changed in production
# (see development.py and production.py).
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Django authentication system
# https://docs.djangoproject.com/en/4.2/topics/auth/

# AUTHENTICATION_BACKENDS = (
#     'axes.backends.AxesBackend',
#     # 'axes.backends.AxesStandaloneBackend',
#     'social_core.backends.github.GithubOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )
#
# PASSWORD_HASHERS = [
#     'django.contrib.auth.hashers.Argon2PasswordHasher',
#     'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#     'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
#     'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
# ]


# Security
# https://docs.djangoproject.com/en/4.2/topics/security/

# SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_HTTPONLY = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
#
# X_FRAME_OPTIONS = 'DENY'

# https://github.com/DmytroLitvinov/django-http-referrer-policy
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
# REFERRER_POLICY = 'same-origin'

# https://github.com/adamchainz/django-permissions-policy#setting
# PERMISSIONS_POLICY: Dict[str, Union[str, List[str]]] = {}  # noqa: WPS234


# Timeouts
# https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-EMAIL_TIMEOUT

EMAIL_TIMEOUT = 5


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# SOCIAL_AUTH_GITHUB_KEY = config('SOCIAL_AUTH_GITHUB_KEY', cast=str)
# SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET', cast=str)
