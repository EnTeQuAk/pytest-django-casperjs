from __future__ import absolute_import

from .fixtures import casper_js


(casper_js)


def pytest_addoption(parser):
    group = parser.getgroup('django_casperjs')


def pytest_configure(config):
    # TODO: Force pytest-django to be loaded
    pass
