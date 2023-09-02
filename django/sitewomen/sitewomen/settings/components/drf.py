# from decouple import config
import mimetypes

DTM_IGNORED_MIGRATIONS = ['0004_auto_20160423_0400', '0005_auto_20160727_2333', '0005_auto_20160727_2333']

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# SOCIAL_AUTH_JSONFIELD_ENABLED = True  устарело
SOCIAL_AUTH_POSTGRES_JSONFIELD_ENABLED = True

mimetypes.add_type("application/javascript", ".js", True)

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.github.GithubOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )


CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
