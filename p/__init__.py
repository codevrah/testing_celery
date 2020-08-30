from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "p.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from .celery import app as celery_app