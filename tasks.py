from celery import Celery

from main import check_table_data

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def run_main():
    check_table_data()
