from __future__ import with_statement

import django
import pytest

from django.conf import settings as real_settings
from django.utils.encoding import force_text
from django.test.client import Client, RequestFactory

from .app.models import Item

from pytest_django_casperjs.compat import urlopen


django  # Avoid pyflakes complaints


@pytest.mark.django_db
class TestCasperJSLiveServer:
    # Partially based on the LiveServer test case from pytest_django'

    def test_url(self, casper_js):
        assert casper_js.url == force_text(casper_js)
