Mechanize_ support for Django testcases.

Testcases are subclasses of DjangoMechanizeTestCase.

The mechanize browser is accessed via self.browser. Your test will fetch
URLs from a virtual server running your Django project. This defaults to
http://localhost:17681 - use self.browser_url() to avoid hardcoding that
address.

e.g:

::
    class MyTestCase(DjangoMechanizeTestCase):
        def test_with_mechanize(self):
            self.browser.open(self.browser_url('/test_view/'))
            self.browser.select_form(name='upload_form')
            self.browser.add_file(StringIO('12341234'), 'text/plain', 'test.txt')
            self.browser.submit()

.. _Mechanize: http://wwwsearch.sourceforge.net/mechanize/
