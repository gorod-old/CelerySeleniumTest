from celery import Celery
from celery.schedules import crontab

from CeleryPack import celeryconfig
from main import check_table_data

app = Celery('tasks')

app.config_from_object(celeryconfig, namespace='CELERY')

app.conf.beat_schedule = {
    'run_channels_pars_msgs': {
        'task': 'CeleryPack.tasks.run_main',
        'schedule': crontab(minute='*/10'),
    }
}
app.conf.timezone = 'UTC'

@app.task
def run_main():
    check_table_data()
