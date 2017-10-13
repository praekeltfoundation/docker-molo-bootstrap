from testtools import matchers as m
from testtools.assertions import assert_that

from fixtures import *  # noqa: We import these so pytest can find them.


class TestApp:
    def test_wagtail_admin_site_live(self, web_client):
        """
        When we get the /admin/ path, we should receive some HTML for the
        Wagtail admin interface.
        """
        response = web_client('/admin/')

        assert_that(response.headers['Content-Type'],
                    m.Equals('text/html; charset=utf-8'))
        assert_that(response.text,
                    m.Contains('<title>Wagtail - Sign in</title>'))

    def test_django_admin_site_live(self, web_client):
        """
        When we get the /django-admin/ path, we should receive some HTML for
        the Django admin interface.
        """
        response = web_client('/django-admin/')

        assert_that(response.headers['Content-Type'],
                    m.Equals('text/html; charset=utf-8'))
        assert_that(response.text,
                    m.Contains('<title>Log in | Django site admin</title>'))
