from pathlib import Path
from django.core.management.utils import get_random_secret_key
import sys
from configparser import ConfigParser, RawConfigParser
import pkg_resources
from .pkgcheck import pkg_check
import importlib.util
from os import getcwd, listdir, makedirs
from os.path import join, isdir


BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_DIR = join(getcwd())

CONFIG = ConfigParser()
CONFIG.read(join(PROJECT_DIR, 'setup.ini'), encoding='utf-8')

SECRET_KEY = get_random_secret_key()

DEBUG = True

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = "core.User"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_filters',
    'rest_framework',
    'bomiot.server.core',
]

PROJECT_NAME = CONFIG.get('project', 'name', fallback='bomiot')

for module in [pkg.key for pkg in pkg_resources.working_set]:
    try:
        settings_name = 'bomiotconf'
        exists = pkg_check(module, settings_name)
        if exists:
            module_import = importlib.import_module(f'{module}.{settings_name}')
            app_mode = module_import.mode_return()
            if app_mode == 'plugins':
                INSTALLED_APPS.append(f'{module}')
            elif app_mode == 'project':
                if PROJECT_NAME != 'bomiot':
                    if module == PROJECT_NAME:
                        project_path = importlib.util.find_spec(PROJECT_NAME).origin
                        list_project_path = Path(project_path).resolve().parent
                        find_apps = [u for u in listdir(list_project_path) if isdir(u)]
                        for app in find_apps:
                            sys.path.insert(0, join(list_project_path, app))
                            if importlib.util.find_spec(f'{PROJECT_NAME}.{app}.apps') is not None:
                                INSTALLED_APPS.append(f'{PROJECT_NAME}.{app}')
        else:
            continue
    except:
        continue
    finally:
        pass

current_path = [p for p in listdir(getcwd()) if isdir(p)]

for module_name in current_path:
    try:
        sys.path.insert(0, join(getcwd()))
        settings_name = 'bomiotconf'
        exists = pkg_check(module_name, settings_name)
        if exists:
            module_import = importlib.import_module(f'{module_name}.{settings_name}')
            app_mode = module_import.mode_return()
            if app_mode == 'plugins':
                INSTALLED_APPS.append(module_name)
            elif app_mode == 'project':
                if PROJECT_NAME != 'bomiot':
                    if module_name == PROJECT_NAME:
                        project_path = join(getcwd(), PROJECT_NAME)
                        find_apps = [u for u in listdir(project_path) if isdir(u)]
                        for app in find_apps:
                            sys.path.insert(0, join(project_path, app))
                            if importlib.util.find_spec(f'{PROJECT_NAME}.{app}.apps') is not None:
                                INSTALLED_APPS.append(f'{PROJECT_NAME}.{app}')
        else:
            continue
    except:
        continue
    finally:
        pass


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bomiot.server.server.urls'

templates_path = join(BASE_DIR.parent, 'templates')

if PROJECT_NAME in [p for p in listdir(getcwd()) if isdir(p)]:
    templates_path = join(join(PROJECT_DIR, 'PROJECT_NAME'), 'templates')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [templates_path],
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

WSGI_APPLICATION = 'bomiot.server.server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
BASE_DB_TABLE = CONFIG.get('db_name', 'name', fallback='bomiot')

DATABASE_MAP = {
    'sqlite': 'django.db.backends.sqlite3',
    'mysql': 'django.db.backends.mysql',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'oracle': 'django.db.backends.oracle',
}

db_engine = CONFIG.get('database', 'engine', fallback='sqlite')
if db_engine == 'sqlite':
    DB_DIR = join(getcwd(), 'dbs')
    exists(DB_DIR) or makedirs(DB_DIR)
    DB_PATH = join(DB_DIR, 'db.sqlite3')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': DB_PATH,
            'OPTIONS': {
                'timeout': 20,
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': DATABASE_MAP[CONFIG['database']['engine']],
            'NAME': CONFIG['database']['name'],
            'USER': CONFIG['database']['user'],
            'PASSWORD': CONFIG['database']['password'],
            'HOST': CONFIG['database']['host'],
            'PORT': CONFIG['database']['port'],
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = CONFIG.getint('local', 'language_code', fallback='en-us')

TIME_ZONE = CONFIG.getint('local', 'time_zone', fallback='UTC')

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = join(getcwd(), 'bomiot_static').replace('\\', '/')
STATICFILES_DIRS = [
    join(BASE_DIR, "static").replace('\\', '/'),
]

MEDIA_URL = 'media/'
MEDIA_ROOT = join(getcwd(), 'media').replace('\\', '/')
exists(MEDIA_ROOT) or makedirs(MEDIA_ROOT)


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

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
    'token',
    'language',
    'operator',
    'device',
    'app-id',
    'event-sign'
)

X_FRAME_OPTIONS = 'SAMEORIGIN'


LOG_PATH = join(getcwd(), 'logs')
exists(LOG_PATH) or makedirs(LOG_PATH)
SERVER_LOGS_FILE = join(LOG_PATH, 'server.log')
ERROR_LOGS_FILE = join(LOG_PATH, 'error.log')
STANDARD_LOG_FORMAT = (
    "[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"
)
CONSOLE_LOG_FORMAT = (
    "[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"
)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": STANDARD_LOG_FORMAT},
        "console": {
            "format": CONSOLE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "file": {
            "format": CONSOLE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": SERVER_LOGS_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 5,  # 最多备份5个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ERROR_LOGS_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 3,  # 最多备份3个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },

    },
    "loggers": {
        "": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
        },
        "django": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
            "propagate": False,
        },
        'django.db.backends': {
            'handlers': ["console", "error", "file"],
            'propagate': False,
            'level': "INFO"
        },
        "uvicorn.error": {
            "level": "INFO",
            "handlers": ["console", "error", "file"],
        },
        "uvicorn.access": {
            "handlers": ["console", "error", "file"],
            "level": "INFO"
        },
    },
}

REST_FRAMEWORK = {
    # AttributeError: ‘AutoSchema’ object has no attribute ‘get_link’
    # DEFAULT SET:
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',
    # EXCEPTION:
    'EXCEPTION_HANDLER': 'bomiot.server.core.my_exceptions.custom_exception_handler',
    # Base API policies:
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
        #'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': ['bomiot.server.core.auth.AsyncAuthentication', ],
    'DEFAULT_PERMISSION_CLASSES': ["bomiot.server.core.permission.AsyncPermission", ],
    'DEFAULT_THROTTLE_CLASSES': ['bomiot.server.core.throttle.AsyncThrottle', ],
    # 'DEFAULT_THROTTLE_RATES': ['utils.throttle.VisitThrottle', ],
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'rest_framework.negotiation.DefaultContentNegotiation',
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'DEFAULT_VERSIONING_CLASS': None,
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 1,  # 默认 None
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        # 'django_filters.rest_framework.backends.DjangoFilterBackend',
    ],
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',
    'NUM_PROXIES': None,
    # Versioning:
    'DEFAULT_VERSION': None,
    'ALLOWED_VERSIONS': None,
    'VERSION_PARAM': 'version',
    # Authentication:
    'UNAUTHENTICATED_USER': 'django.contrib.auth.models.AnonymousUser',
    'UNAUTHENTICATED_TOKEN': None,
    # View configuration:
    'VIEW_NAME_FUNCTION': 'rest_framework.views.get_view_name',
    'VIEW_DESCRIPTION_FUNCTION': 'rest_framework.views.get_view_description',
    'NON_FIELD_ERRORS_KEY': 'non_field_errors',
    # Testing
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer'
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'multipart',
    # Hyperlink settings
    'URL_FORMAT_OVERRIDE': 'format',
    'FORMAT_SUFFIX_KWARG': 'format',
    'URL_FIELD_NAME': 'url',
    # Encoding
    'UNICODE_JSON': True,
    'COMPACT_JSON': True,
    'STRICT_JSON': True,
    'COERCE_DECIMAL_TO_STRING': True,
    'UPLOADED_FILES_USE_URL': True,
    # Browseable API
    'HTML_SELECT_CUTOFF': 1000,
    'HTML_SELECT_CUTOFF_TEXT': "More than {count} items...",
    # Schemas
    'SCHEMA_COERCE_PATH_PK': True,
    'SCHEMA_COERCE_METHOD_NAMES': {
        'retrieve': 'read',
        'destroy': 'delete'
    },
}

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]

USER_JWT_TIME = CONFIG.getint('jwt', 'user_jwt_time', fallback=1000000)

ALLOCATION_SECONDS = CONFIG.getint('throttle', 'allocation_seconds', fallback=1)
THROTTLE_SECONDS = CONFIG.getint('throttle', 'throttle_seconds', fallback=10)

ALLOWED_IMG = CONFIG.get('image_upload', 'suffix_name', fallback='jpg, jpeg, gif, png, bmp, webp').split(',')

DATA_UPLOAD_MAX_MEMORY_SIZE = None