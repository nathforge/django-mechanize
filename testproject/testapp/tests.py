from djangomechanize import DjangoMechanizeTestCase
from cStringIO import StringIO
import socket


class TestCaseTestCase(DjangoMechanizeTestCase):
    def test_upload(self):
        # Go to the form and upload a file. The uploaded file must have a
        # filename, or Django ignores it.
        self.browser.open(self.browser_url('/'))
        self.browser.select_form(name='upload_form')
        self.browser.add_file(StringIO('12341234'), 'text/plain', 'test.txt')
        self.browser.submit()
        
        # Page should contain the message "this field is required", as we
        # didn't enter anything for the text field.
        assert self.browser.response().read().count('This field is required') == 1
        
        # Enter values for the file field and text field, and submit.
        self.browser.select_form(name='upload_form')
        self.browser.add_file(StringIO('12341234'), 'text/plain', 'test.txt')
        self.browser['text'] = 'text'
        self.browser.submit()
        
        # The form should now validate.
        assert 'Success!' in self.browser.response().read()
    
    def test_wsgi_intercept(self):
        # Check that we're not running a live HTTP server.
        self.assertRaises(socket.error, lambda: socket.socket().connect(self.TEST_ADDRESS))
