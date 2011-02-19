from django.core.management import call_command
import os
import os.path
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'testproject'))

call_command('test')
