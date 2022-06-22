"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%s_g+nzeh06=h!*#3%5=(6d#z1z-6mz_l!jwx@v05=!wq2k2z_'

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
    'rest_framework',
     # Add our new application
    'api.apps.ApiConfig'
    # 'backend',
    # 'api'
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

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Media settings
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
"""
All uploaded data containing media (images, videos, files) will be moved to the MEDIA_ROOT folder.

e.g.    I upload a file called 'AmbassadorDP.png', to use as the property for an ImageField. 
        The ImageField has the parameter " upload_to = 'Ambassador Image/' " 
        The file will now be found at: BASE_DIR/media/Ambassador Image/AmbassadorDP.png
"""
MEDIA_URL = 'media/'
"""
In development only: media files can be accessed from the media URL.

e.g.    The file is found at: BASE_DIR/media/Ambassador Image/AmbassadorDP.png
        When running the development server, the image can be retrieved from the browser at the URL:
            <base URL>/media/Ambassador%20Image/AmbassadorDP.png

Requires a static URL to be addded in urls.py: "urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"

Important: media files should not be served from the django backend in production. A proper CDN is needed, e.g. Amazon S3.
In production, after receiving a file, django should upload what it receives to the CDN, using whatver API they provide.
The local database entry should be updated to have a reference to the final URL provided by the CDN to access the file.
Finally, the front end accesses the file/image/video using the URL to the CDN, NOT through the django backend.
The front end should be able to receive that URL from the djangorestframework API response.
"""



