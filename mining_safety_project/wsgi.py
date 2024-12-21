"""
WSGI config for mining_safety_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from waitress import serve

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mining_safety_project.settings')

application = get_wsgi_application()

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=10000)

