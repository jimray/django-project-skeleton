from .base import *

DEBUG = True
TEMPLATE_DEBUG = True


INSTALLED_APPS += (
    'debug_toolbar',
)


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Static files (CSS, JavaScript, Images)
# Great for local development, not terribly well suited for production
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)


# DEBUG TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)