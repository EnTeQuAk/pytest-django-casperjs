from django.conf import settings
import os
import os.path


def pytest_configure(config):
    test_db = os.environ.get('DB', 'sqlite')
    if test_db == 'mysql':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings_mysql'
        settings.DATABASES['default'].update({
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pytest_django_casperjs_test',
            'USER': 'root',
        })
    elif test_db == 'postgres':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings_postgres'
        settings.DATABASES['default'].update({
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'postgres',
            'NAME': 'pytest_django_casperjs_test',
        })
    elif test_db == 'sqlite':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings_sqlite'
        settings.DATABASES['default'].update({
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        })
    else:
        raise RuntimeError('Unsupported database configuration')

    # override a few things with our test specifics
    settings.INSTALLED_APPS = tuple(settings.INSTALLED_APPS) + (
        'tests',
    )
