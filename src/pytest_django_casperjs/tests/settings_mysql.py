from .settings_base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pytest_django_casperjs_test' + db_suffix,
        'HOST': 'localhost',
        'USER': 'root',
    },
}