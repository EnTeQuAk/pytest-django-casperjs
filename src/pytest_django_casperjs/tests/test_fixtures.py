from __future__ import with_statement

import django
import pytest

from django.conf import settings as real_settings
from django.utils.encoding import force_text
from django.test.client import Client, RequestFactory
from django.test.testcases import connections_support_transactions

from .app.models import Item

from pytest_django_casperjs.compat import urlopen


django  # Avoid pyflakes complaints


class TestCasperJSLiveServer:
    # Partially based on the LiveServer test case from pytest_django'

    pytestmark = [
        pytest.mark.django_db()
    ]

    def test_url(self, casper_js):
        assert casper_js.url == force_text(casper_js)

    def test_db_changes_visibility(self, casper_js):
        response_data = urlopen(casper_js + '/item_count/').read()
        assert force_text(response_data) == 'Item count: 0'
        Item.objects.create(name='foo')
        response_data = urlopen(casper_js + '/item_count/').read()
        assert force_text(response_data) == 'Item count: 1'

    def test_fixture_db(self, db, casper_js):
        Item.objects.create(name='foo')
        response_data = urlopen(casper_js + '/item_count/').read()
        assert force_text(response_data) == 'Item count: 1'

    def test_fixture_transactional_db(self, transactional_db, casper_js):
        Item.objects.create(name='foo')
        response_data = urlopen(casper_js + '/item_count/').read()
        assert force_text(response_data) == 'Item count: 1'

    @pytest.fixture
    def item(self):
        # This has not requested database access so should fail.
        # Unfortunately the _live_server_helper autouse fixture makes this
        # test work.
        with pytest.raises(pytest.fail.Exception):
            Item.objects.create(name='foo')

    @pytest.mark.xfail
    def test_item(self, item, casper_js):
        # test should fail/pass in setup
        pass

    @pytest.fixture
    def item_db(self, db):
        return Item.objects.create(name='foo')

    def test_item_db(self, item_db, casper_js):
        response_data = urlopen(casper_js + '/item_count/').read()
        assert force_text(response_data) == 'Item count: 1'

    @pytest.fixture
    def item_transactional_db(self, transactional_db):
        return Item.objects.create(name='foo')

    def test_item_transactional_db(self, item_transactional_db, casper_js):
        response_data = urlopen(casper_js + '/item_count/').read()
        assert force_text(response_data) == 'Item count: 1'
