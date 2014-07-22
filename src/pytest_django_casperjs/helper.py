import sys
import os

from subprocess import Popen, PIPE

import pytest
from pytest_django.live_server_helper import LiveServer

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.contrib.staticfiles.views import serve
from django.test import LiveServerTestCase
from django.utils.http import http_date
from django.conf import settings


def staticfiles_handler_serve(self, request):
    import time
    resp = serve(request, self.file_path(request.path), insecure=True)
    if resp.status_code == 200:
        resp["Expires"] = http_date(time.time() + 24 * 3600)
    return resp


class CasperJSLiveServer(LiveServer):
    """Helper class that wraps CaperJS based on the Django live server."""

    use_phantom_disk_cache = False

    def __init__(self, *args, **kwargs):
        super(CasperJSLiveServer, self).__init__(*args, **kwargs)
        if self.use_phantom_disk_cache:
            StaticFilesHandler.serve = staticfiles_handler_serve

        # TODO: Those are still kinda opinionated, break up for more configurability
        if os.environ.get('NPM_ROOT', None):
            self.prefix = os.path.abspath(os.environ['NPM_ROOT']) + '/.bin/'
            os.environ['PHANTOMJS_EXECUTABLE'] = os.path.abspath(
                os.environ['NPM_ROOT'] + '/.bin/phantomjs'
            )
        else:
            self.prefix = ''

    def casper(self, test_filename, cookies=None, **kwargs):
        """CasperJS test invoker.

        Takes a test filename (.js) and optional arguments to pass to the
        casper test.

        Returns True if the test(s) passed, and False if any test failed.

        Since CasperJS startup/shutdown is quite slow, it is recommended
        to bundle all the tests from a test case in a single casper file
        and invoke it only once.

        :param cookie: ...
        """

        kwargs.update({
            'load-images': 'no',
            'disk-cache': 'yes' if self.use_phantom_disk_cache else 'no',
            'ignore-ssl-errors': 'yes',
            'url-base': self.url
        })

        cn = settings.SESSION_COOKIE_NAME

        if cookies and cn in cookies:
            kwargs['cookie-' + cn] = cookies[cn].value

        cmd = [self.prefix + 'casperjs', 'test', '--no-colors']

        # TODO: make configurable
        base_path = os.path.abspath(os.path.dirname(test_filename))
        xunit_path = os.path.join(
            base_path,
            'junit-' + os.path.basename(test_filename) + '.xml')
        kwargs['xunit'] = xunit_path

        cmd.extend([('--%s=%s' % i) for i in kwargs.iteritems()])
        cmd.append(test_filename)

        process = Popen(
            cmd,
            stdout=PIPE,
            stderr=PIPE,
            cwd=os.path.dirname(test_filename))

        out, err = process.communicate()

        # TODO: Use logging
        sys.stdout.write('====== CASPERJS DEBUG OUTPUT =========\n\n')
        sys.stdout.write(out)
        sys.stderr.write(err)
        sys.stdout.write('\n\n====== CASPERJS DEBUG OUTPUT END =========\n\n')

        return process.returncode == 0

    def __repr__(self):
        return '<CasperJSLiveServer listening at %s>' % self.url

