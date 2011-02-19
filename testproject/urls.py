from django.conf.urls.defaults import *


urlpatterns = patterns('',
    ('^$', 'testapp.views.test_view'),
)
