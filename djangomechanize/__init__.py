from django.core.handlers.wsgi import WSGIHandler
import unittest
import urlparse
import wsgi_intercept, wsgi_intercept.mechanize_intercept


class DjangoMechanizeTestCase(unittest.TestCase):
    """
    Mechanize support for Django testcases.
    <http://wwwsearch.sourceforge.net/mechanize/>
    
    Testcases are subclasses of DjangoMechanizeTestCase.
    
    The mechanize browser is accessed via self.browser. Your test will fetch
    URLs from a virtual server running your Django project. This defaults to
    http://localhost:17681 - use self.browser_url() to avoid hardcoding that
    address.
    
    e.g:
        class MyTestCase(DjangoMechanizeTestCase):
            def test_with_mechanize(self):
                self.browser.open(self.browser_url('/test_view/'))
                self.browser.select_form(name='upload_form')
                self.browser.add_file(StringIO('12341234'), 'text/plain', 'test.txt')
                self.browser.submit()
    """
    
    TEST_ADDRESS = ('localhost', 17681,)
    
    def setUp(self):
        self.browser = self.create_browser()
    
    def browser_url(self, url):
        """
        Create a URL for the virtual WSGI server.
        e.g browser_url('/'), browser_url(reverse('my_view'))
        """
        return urlparse.urljoin('http://%s:%d/' % self.TEST_ADDRESS, url)
    
    def create_browser(self):
        """
        Create a Mechanize browser. Intercepts requests to
        http://localhost:17681 and sends them to Django's WSGI handler.
        This can be overridden via self.TEST_ADDRESS, if your tests need to
        use an actual server at this address:port.
        
        Robots.txt is disabled, as it'll likely throw a 404 error in your test.
        If you need to test your robots file, use
        self.browser.set_handle_robots(True).
        """
        host, port = self.TEST_ADDRESS
        wsgi_intercept.add_wsgi_intercept(host, port, WSGIHandler)
        browser = wsgi_intercept.mechanize_intercept.Browser()
        browser.set_handle_robots(False)
        return browser
