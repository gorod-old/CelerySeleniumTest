from celery import Celery

from main import check_table_data

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def run_main():
    check_table_data()
