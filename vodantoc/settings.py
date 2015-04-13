from django.utils.translation import gettext_noop
import os
gettext = lambda s: s
PROJECT_ROOT = PROJECT_PATH = PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Django settings for my_demo project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('vovietname', 'paul.guichon@iedparis8.net')
)

MANAGERS = ADMINS


LOCALE_PATHS = (PROJECT_ROOT+"/locale",)
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['test-vodantoc.com', 'vodantoc.com', 'vodantoc.fr', 'www.vodantoc.com', 'vodantoc.fr']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'my_demo', 'static'),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^p@e&rmlq+!(5mxiytw=cuw@lseplolyss$*4qbo^@zobcfc-z'

# List of callables that know how to import templates from various sources.




ROOT_URLCONF = 'vodantoc.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'vodantoc.wsgi.application'





SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    'app_namespace.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS = (

    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',

    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'zinnia.context_processors.version',
)

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

INSTALLED_APPS = (
    'cms',
    'blog_entry',
    'zinnia_bootstrap',
    'app_namespace',
    "base",
    'tagging',
    'easy_maps',
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'filer',
    'django_extensions',
    'easy_thumbnails',

    'mptt',
    'menus',
    'south',
    'sekizai',
    'djangocms_style',
    'djangocms_column',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'vodantoc',
    'zinnia',
    'cmsplugin_zinnia',
    'calendarium',
    'reversion',
)

LANGUAGES = [
    ('fr', gettext_noop('French')),
]

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'fr',
            'hide_untranslated': False,
            'name': gettext('fr'),
            'redirect_on_fallback': True,
        },
        # {
        #     'public': True,
        #     'code': '',
        #     'hide_untranslated': False,
        #     'name': gettext(''),
        #     'redirect_on_fallback': True,
        # },
    ],
}

CMS_TEMPLATES = (
    ('template_1.html', 'Template with sidebar'),
    ('template_2.html', 'Template simple'),
    ('accueil.html', 'Template de l\'accueil'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default':
        {'ENGINE': 'django.db.backends.sqlite3', 'NAME':'site_vo.db', 'HOST': 'localhost', 'USER': '', 'PASSWORD': '', 'PORT': ''}
}


CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_URL, 'uploads')
CKEDITOR_CONFIGS = {
           'default': {
               'toolbar': 'Complete', # Other Option is 'Full'
               'height': 300,
               'width': 0, # Full Width
           },
       }
CKEDITOR_IMAGE_BACKEND = 'pillow'


try:
    from local_settings import *
except ImportError:
    pass

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
# ZINNIA_ENTRY_BASE_MODEL = 'base.models.EntryBase'

ACCOUNT_ACTIVATION_DAYS = 1

ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'

TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plug'
CMSPLUGIN_FILER_FOLDER_VIEW_OPTIONS = (("list", "Liste"), ("list_z", "Liste blog"))
STYLE_CHOICES = (("list", "Liste"), ("list_z", "Liste blog"))
CMSPLUGIN_ZINNIA_APP_MENUS = []
SOUTH_MIGRATION_MODULES = {
        'easy_thumbnails': 'easy_thumbnails.south_migrations',
    }
