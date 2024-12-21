"""
WSGI config for mining_safety_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# mining_safety_project/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
=======
from waitress import serve
>>>>>>> eaf0b04b0ec7948f2daf38a93a6c21582c7377b2

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mining_safety_project.settings')

application = get_wsgi_application()

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=10000)

