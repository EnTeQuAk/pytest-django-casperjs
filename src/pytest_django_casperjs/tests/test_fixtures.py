import pytest

from django.utils.encoding import force_text


@pytest.mark.django_db
class TestCasperJSLiveServer:
    # Partially based on the LiveServer test case from pytest_django'

    def test_url(self, casper_js):
        assert casper_js.url == force_text(casper_js)
