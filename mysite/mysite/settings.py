#!coding=utf-8
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4@01u6jlly!dr*x&91$p@bqo4w(%0t0g8zp+6g9s650(&glpkv'

# SECURITY WARNING: don't run with debug turned on in production!
import socket
if socket.gethostname() == 'dizzy-pc':
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = True

# 建议使用官方文档那种，将模板及静态文件放入到相应的应用中
# TEMPLATE_DIRS = os.path.join(BASE_DIR, 'templates')

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'))

ALLOWED_HOSTS = ['127.0.0.1', '.jd-app.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #add by dizzy in 2014-07-29 19:36:23
    'dlog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#        # 'ENGINE': 'django.db.backends.sqlite3',
#        # 'NAME': 'dlog.sqlite3',
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'dlog',
#        'USER': 'root',
#        'PASSWORD': '944898186',
#        'HOST': 'localhost',
#        'PORT': '3306',
#     }
# }


# 线上数据库的配置
if socket.gethostname() != 'dizzy-pc':
    MYSQL_HOST = 'w.rdc.sae.sina.com.cn'
    MYSQL_PORT = '3307'
    MYSQL_USER = '353nym1zo0'
    MYSQL_PASS = '4wl34xly1j01xhwz3i1ziii5y5z3hzhj4014hzk2'
    MYSQL_DB = 'tiny234'
else:
    MYSQL_DB = 'dlog'
    MYSQL_USER = 'root'
    MYSQL_PASS = '944898186'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'


# from sae._restful_mysql import monkey
# monkey.patch()

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     MYSQL_DB,
        'USER':     MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST':     MYSQL_HOST,
        'PORT':     MYSQL_PORT,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
