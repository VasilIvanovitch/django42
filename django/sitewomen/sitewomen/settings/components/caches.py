# Caching
# https://docs.djangoproject.com/en/4.2/topics/cache/

# настройка по умолчанию
CACHES = {
    'default': {
        # TODO: use some other cache in production,
        # like https://github.com/jazzband/django-redis
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}


# django-axes
# https://django-axes.readthedocs.io/en/latest/4_configuration.html#configuring-caches

# AXES_CACHE = 'default'
#
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",  # Здесь укажите свой хост и порт Redis
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }


# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://172.0.0.1:6379",
#         'OPTIONS': {
#             'db': 2
#         }
#     }
# }

# django.core.cache.backends.redis.RedisCache

# PRICE_CACHE_NAME = 'price_cache'
