from Ecommerce.config.base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS        = ['0.0.0.0','localhost', 'localhost:85', '127.0.0.1', env('SERVER', default='127.0.0.1')]
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

INTERNAL_IPS = ['127.0.0.1','0.0.0.0']
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
}

