from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SAWAABA_CELERY.settings')

app = Celery('SAWAABA_CELERY')
app.conf.broker_connection_max_retries = None  # Infinite retries
app.conf.broker_connection_timeout = 30  # Increase timeout to 30 seconds
app.conf.broker_heartbeat = 30  # Heartbeat interval in seconds
app.log.setup_logging_subsystem(loglevel='DEBUG')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
