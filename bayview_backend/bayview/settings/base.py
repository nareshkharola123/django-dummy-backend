"""
Django settings for bayview project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f*jy-dnheg4idd)27%$lnfhh4@vcd3%%7(=d_hogfb!)*he--+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = []

# tenant-schema configurations


# SHARED_APPS = (
#     'tenant_schemas',  # mandatory, should always be before any django app
#     'users', # you must list the app where your tenant model resides in
#     'business_units',
#     'consumers',
#     'django_extensions',
#     'rest_framework',
#     'safedelete',
#     'django.contrib.contenttypes',

#     # everything below here is optional
#     'django.contrib.auth',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'django.contrib.messages',
#     'django.contrib.admin',
# )


# TENANT_APPS = (
#     # The following Django contrib apps must be in TENANT_APPS
#     "django.contrib.contenttypes",
#     "django.contrib.auth",
#     "customers",
#     "templates_app",
#     "campaigns",
# )

# TENANT_MODEL = "business_units.BusinessUnit"

# DEFAULT_FILE_STORAGE = "tenant_schemas.storage.TenantFileSystemStorage"


# Application definition

INSTALLED_APPS = [
    # 'tenant_schemas', # mandatory, should always be before any django app
    # django default app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    # installed apps
    'rest_framework',
    'corsheaders',
    'django_extensions',
    'safedelete',
    # custom apps
    'users',
    'business_units',
    'customers',
    'templates_app',
    'campaigns',
    'consumers',
]

SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"


MIDDLEWARE = [
    # 'tenant_schemas.middleware.TenantMiddleware',
    # 'bayview.tenant_middleware.XHeaderTenantMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bayview.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bayview.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # NOQA
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Auth User Model
AUTH_USER_MODEL = 'users.User'

# rest_framework token auth
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'users.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'bayview.jwt_authentication.JWTAuthentication',
    ),
}

# redis configurations
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_LOCATION"),
    }
}


# corsheaders

# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]

CORS_ORIGIN_ALLOW_ALL = True


CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'access-control-allow-origin'
)

# CORS_ORIGIN_WHITELIST = [
#     os.getenv("CORS_ORIGIN_WHITELIST_DOMAIN"),
# ]

# email configurations

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'manthan.anejaa@sourcefuse.com'
EMAIL_HOST_PASSWORD = 'Manthan1@5'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# database configurations

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': os.getenv("DATABASE_PORT"),
    }
}


# DATABASE_ROUTERS = (
#     'tenant_schemas.routers.TenantSyncRouter',
# )
