import os
import os.path


def pytest_configure(config):
    test_db = os.environ.get('DB', 'sqlite')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'pytest_django_casperjs.tests.settings'  # noqa
    from django.conf import settings
    if test_db == 'postgresql':
        settings.DATABASES['default'].update({
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'postgres',
            'NAME': 'pytest_django_casperjs_test',
        })
    elif test_db == 'mysql':
        settings.DATABASES['default'].update({
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'root',
            'NAME': 'pytest_django_casperjs_test',
        })
    elif test_db == 'sqlite':
        settings.DATABASES['default'].update({
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        })
    else:
        raise RuntimeError('Unsupported database configuration %s' % test_db)
