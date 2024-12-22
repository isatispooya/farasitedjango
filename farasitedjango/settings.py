"""
Django settings for farasitedjango project.

Generated by 'django-admin startproject' using Django 4.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import environ

from pathlib import Path

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u69^8*1=n6o3f*^hj_blrt_*0846r#n-mix332zdtn9#$&8qa3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')


CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')




ALLOWED_HOSTS = ['*',
                 'farasite.fidip.ir',
                 'https://farasite.fidip.ir',
                 'localhost',
                 'http://localhost',
                 'http://localhost:3000',
                 '109.125.151.26',
                'ipmill.isatispooya.com',
                'fid.isatispooya.com',
                'pardisan.isatispooya.com',
                'insurce.isatispooya.com',
                 ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'website',
    'rest_framework',
    'corsheaders',
    'colorfield',
    'django_summernote',
    'menu',
    'structure',
    'superproduct',
    'introduction',
    'chart',
    'vision',
    'brief',
    'bourse',
    'supercart',
    'tinymce',
    'education',
    'blog',

]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'API Documentation',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'farasitedjango.urls'

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

WSGI_APPLICATION = 'farasitedjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
SITE_TITLE = "فراسایت"
SITE_HEADER = "فراسایت" 

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")

]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=env('EMAIL_PORT')
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True


SUMMERNOTE_CONFIG = {
    'width': '800',
    'height': '600',
    'toolbar': [
        ['style', ['style']],
        ['font', ['bold', 'italic', 'underline', 'clear']],
        ['fontname', ['fontname']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['insert', ['link', 'picture', 'video', 'table', 'hr']],
        ['view', ['fullscreen', 'codeview']],
        ['help', ['help']],
    ],
}


TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 600,
    'menubar': 'file edit view insert format tools table help',
    'plugins': 'advlist autolink lists link image charmap print preview hr anchor pagebreak imagetools',
    'toolbar': 'undo redo | formatselect | bold italic backcolor | \
                 alignleft aligncenter alignright alignjustify | \
                 bullist numlist outdent indent | removeformat | image | help',
    'image_advtab': True,
    'file_picker_callback': '''
        function(callback, value, meta) {
            if (meta.filetype == 'image') {
                var input = document.createElement('input');
                input.setAttribute('type', 'file');
                input.setAttribute('accept', 'image/*');
                input.onchange = function() {
                    var file = this.files[0];
                    var reader = new FileReader();
                    reader.onload = function () {
                        callback(reader.result, {
                            alt: file.name
                        });
                    };
                    reader.readAsDataURL(file);
                };
                input.click();
            }
        }
    ''',
}

USE_TZ = True  
TIME_ZONE = 'UTC'