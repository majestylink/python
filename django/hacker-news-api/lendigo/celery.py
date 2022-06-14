import os

from celery.schedules import crontab
from environs import Env

# from src.tasks import create_daily_stats

from celery import Celery
env = Env()
env.read_env()

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lendigo.settings')

# app = Celery('lendigo', broker='amqp://guest:@localhost:5672//')
app = Celery('lendigo', broker=env.str("BROKER_URL"))

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
