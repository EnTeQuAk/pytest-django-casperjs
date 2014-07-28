import os

import pytest
from pytest_django.lazy_django import skip_if_no_django


@pytest.fixture(scope='session')
def casper_js(request):
    skip_if_no_django()

    from pytest_django_casperjs.helper import CasperJSLiveServer

    addr = request.config.getvalue('liveserver')

    if not addr:
        addr = os.getenv('DJANGO_TEST_LIVE_SERVER_ADDRESS')
    if not addr:
        addr = 'localhost:8081,8100-8200'

    server = CasperJSLiveServer(addr)
    request.addfinalizer(server.stop)

    return server
