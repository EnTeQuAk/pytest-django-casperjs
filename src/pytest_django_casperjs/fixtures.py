import os

import pytest
from pytest_django.lazy_django import skip_if_no_django

from pytest_django_casperjs.helper import CasperJSLiveServer


@pytest.fixture(scope='session')
def casper_js(request):
    skip_if_no_django()

    addr = request.config.getvalue('liveserver')
    if not addr:
        addr = os.getenv('DJANGO_TEST_LIVE_SERVER_ADDRESS')
    if not addr:
        addr = 'localhost:8081,8100-8200'

    server = CasperJSLiveServer(addr)
    request.addfinalizer(server.stop)

    return server


@pytest.fixture(autouse=True, scope='function')
def _casper_js_live_server_helper(request):
    if 'capser_js' in request.funcargnames:
        request.getfuncargvalue('transactional_db')
