from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '!$40t+%!n8-7@v@p1)rm66#dyi6%pkyviv@e#fkyd1*)m-eit)'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'admin_shortcuts',
    'vali',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'big_shop',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop_telegram_bot.urls'

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

WSGI_APPLICATION = 'shop_telegram_bot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'big_shop', 
        'USER': 'postgres', 
        'PASSWORD': 'sc0der',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
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

# cors configurations
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
       'http://localhost:4200',
)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


VALI_CONFIG = {
        'theme': 'default',
        'dashboard': {
            'name': 'Панель управление',
            'url': '/vali/dashboard/',
            'subtitle': 'Dashboard view with all statistics',
            'site_name': "'Большой'- Бот",
            'url_image_profile': 'https://avatars.githubusercontent.com/u/44986984?v=4'
        },
        # 'fieldset': {
        #     'fields': ['user_permissions', 'permissions']
        # },
        # 'applist': {
        #     'order': "registry", "group": False
        # }
    }  

ADMIN_SHORTCUTS = [
    {
        'title': "'Большой' Интернет Магазин",
        'shortcuts': [
            {
                'title': 'Заказы',
                'url_name': 'admin:index',
            },
            {
                'title': 'Files',
                'url_name': 'admin:index',
            },
            {
                'title': 'Contact forms',
                'icon': 'columns',
                'url_name': 'admin:index',
                'count_new': '300',
            },
            {
                'title': 'Products',
                'url_name': 'admin:index',
            },
            {
                'title': ('Orders'),
                'url_name': 'admin:index',
                'count_new': '12',
            },
        ]
    },
]

ADMIN_SHORTCUTS_SETTINGS = {
    'show_on_all_pages': False,
    'hide_app_list': False,
    'open_new_window': False,
}