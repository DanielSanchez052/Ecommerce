from Ecommerce.config.base import *

DEBUG = env('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS        = ['localhost', 'localhost:85', '127.0.0.1', env('SERVER', default='127.0.0.1')]
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1', 'https://' + env('SERVER', default='127.0.0.1')]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':env('DB_NAME'),
        'USER':env('DB_USER'),
        'PASSWORD':env('DB_PASS'),
        'HOST':env('DB_HOST'),
        'PORT':env('DB_PORT')
    }
}
