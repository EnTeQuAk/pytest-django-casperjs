#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


version = '0.1.0'


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m "version %s"' % (version, version))
    print('  git push --tags')
    sys.exit()


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fobj:
        return fobj.read()


test_requires = [
    'tox>=1.7.1,<1.8',
    'py>=1.4.20,<1.5',
    'pyflakes>=0.8.1,<0.9',
    'coverage>=3.7.1,<3.8',
    'pytest>=2.5.2,<2.6',
    'pytest-cache>=1.0,<2.0',
    'pytest-cov>=1.6,<1.7',
    'pytest-flakes>=0.2,<1.0',
    'pytest-pep8>=1.0.5,<1.1',
    'pytest-django>=2.6.1,<2.7',
    'python-coveralls>=2.4.2,<2.5',
    'coverage>=3.7.1,<3.8',
    'pep8>=1.4.6,<1.5',
]


install_requires = [
    'django>=1.5',
]


docs_requires = [
    'sphinx',
    'sphinx_rtd_theme'
]


readme =  read('README.rst')
changelog = read('CHANGELOG.rst').replace('.. :changelog:', '')


setup(
    name='pytest-django-casperjs',
    version='0.1.0',
    description='Integrate CasperJS with your django tests as a pytest fixture.',
    long_description=readme + '\n\n' + changelog,
    author='Christopher Grebs',
    author_email='cg@webshox.org',
    url='https://github.com/EnTeQuAk/pytest-django-casperjs/',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    test_suite='.',
    tests_require=test_requires,
    install_requires=install_requires,
    extras_require={
        'docs': docs_requires,
        'tests': test_requires,
        'postgresql': ['psycopg2'],
        'mysql': ['PyMySQL'],
    },
    zip_safe=False,
    license='BSD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    # the following makes a plugin available to pytest
    entry_points = {
        'pytest11': [
            'django_casperjs = pytest_django_casperjs.plugin',
        ]
    },
)
