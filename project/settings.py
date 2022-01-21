"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=4p+jm%jfut4doc1no!xomnvmwi-+!=c#2-v&5xjhr6*)eub=k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #for django alluth
    'django.contrib.sites',


    # My apps
    'blog.apps.BlogConfig',
    'blog_api.apps.BlogApiConfig',
    

    # https://www.django-rest-framework.org/#installation
    'rest_framework',


    # authtoken app which generates the tokens on the server.
    # It comes included with Django REST Framework but must be added to our
    # INSTALLED_APPS setting """
    # https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    'rest_framework.authtoken',



    # https://django-rest-swagger.readthedocs.io/en/latest/
    'rest_framework_swagger',
    

    # https://django-rest-auth.readthedocs.io/en/latest/installation.html
    'rest_auth',
    'rest_auth.registration',
    

    # https://django-allauth.readthedocs.io/en/latest/installation.html
    'allauth',
    'allauth.account',
    'allauth.socialaccount',   
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'



REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.AllowAny',     # default
        'rest_framework.permissions.IsAuthenticated',
    ],


    'DEFAULT_AUTHENTICATION_CLASSES': [
        
        # Sessions are used to power the Browsable API and the ability to log in and log out of it.
        # 'rest_framework.authentication.SessionAuthentication',  # default
        
        # BasicAuthentication is used to pass the session ID in the HTTP headers for the API itself.
        # 'rest_framework.authentication.BasicAuthentication',    # default

        # Simple JWT settings for authentication 
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],


    'DEFAULT_SCHEMA_CLASS': [
        'rest_framework.schemas.coreapi.AutoSchema'
    ],

}

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # new

SITE_ID = 1 

REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }