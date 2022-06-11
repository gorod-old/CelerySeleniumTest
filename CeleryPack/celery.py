from celery import Celery
from celery.schedules import crontab

from CeleryPack import celeryconfig


app = Celery('celery', broker='redis://localhost:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object(celeryconfig, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run_channels_pars_msgs': {
        'task': 'CeleryPack.tasks.run_main',
        'schedule': crontab(minute='*/10'),
    },
    # 'run_channels_pars_msgs_normal': {
    #     'task': 'main.tasks.run_pars_msgs_normal',
    #     'schedule': crontab(minute=0, hour='*/3'),
    # },
    # 'run_channels_pars_users': {
    #     'task': 'main.tasks.run_pars_users',
    #     'schedule': crontab(minute=30, hour='*/6'),
    # },
    # 'check_temp_users': {
    #     'task': 'user_auth.tasks.check_temp_users',
    #     'schedule': crontab(minute=0, hour='*/1'),
    # }
}
app.conf.timezone = 'UTC'

