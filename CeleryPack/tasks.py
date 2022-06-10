from CeleryPack.celery import app
from main import check_table_data


@app.task(queue='default', routing_key='default')
def run_main():
    check_table_data()
