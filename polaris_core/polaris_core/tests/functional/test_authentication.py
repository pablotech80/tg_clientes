# -*- coding: utf-8 -*-
"""
Integration tests for the :mod:`repoze.who`-powered authentication sub-system.

As polaris-core grows and the authentication method changes, only these tests
should be updated.

"""
from __future__ import unicode_literals

from polaris_core.tests import TestController


class TestAuthentication(TestController):
    """
    Tests for the default authentication setup.

    If your application changes how the authentication layer is configured
    those tests should be updated accordingly
    """

    application_under_test = 'main'

    def test_voluntary_login(self):
        """Voluntary logins must work correctly"""
        # Going to the login form voluntarily:
        resp = self.app.get('/login', status=200)
        form = resp.form
        # Submitting the login form:
        form['login'] = 'manager'
        form['password'] = 'managepass'
        post_login = form.submit(status=302)
        # Being redirected to the home page:
        assert post_login.location.startswith('http://localhost/post_login')
        home_page = post_login.follow(status=302)
        assert (
            'authtkt' in home_page.request.cookies
        ), 'Session cookie was not defined: %s' % home_page.request.cookies
        assert home_page.location, 'http://localhost/'

    def test_logout(self):
        """Logouts must work correctly"""
        # Logging in voluntarily the quick way:
        resp = self.app.get('/login_handler?login=manager&password=managepass',
                            status=302)
        resp = resp.follow(status=302)
        assert (
            'authtkt' in resp.request.cookies
        ), 'Session cookie was not defined: %s' % resp.request.cookies
        # Logging out:
        resp = self.app.get('/logout_handler', status=302)
        assert resp.location.startswith('http://localhost/post_logout')
        # Finally, redirected to the home page:
        home_page = resp.follow(status=302)
        authtkt = home_page.request.cookies.get('authtkt')
        assert (
            not authtkt or authtkt == 'INVALID'
        ), 'Session cookie was not deleted: %s' % home_page.request.cookies
        assert home_page.location == 'http://localhost/'

    def test_failed_login_keeps_username(self):
        """Wrong password keeps user_name in login form"""
        resp = self.app.get('/login_handler?login=manager&password=badpassword',
                            status=302)
        resp = resp.follow(status=200)
        assert 'Invalid Password' in resp, resp
        assert resp.form['login'].value == 'manager'
