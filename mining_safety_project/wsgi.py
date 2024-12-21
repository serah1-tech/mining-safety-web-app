import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'application' callable.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mining_safety_project.settings')

# Get the WSGI application.
application = get_wsgi_application()
