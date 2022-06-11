from main import setup
from kombu import Queue, Exchange

# redis and celery
REDIS_HOST = setup.REDIS_HOST
REDIS_PORT = setup.REDIS_PORT
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
result_backend = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
accept_content = ['application/json']
result_serializer = 'json'
task_serializer = 'json'
timezone = setup.TIME_ZONE

task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('for_parsers', Exchange('for_parsers'), routing_key='for_parsers'),
)
task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'
