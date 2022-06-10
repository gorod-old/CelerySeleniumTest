from main import setup
from kombu import Queue, Exchange

# redis and celery
REDIS_HOST = setup.REDIS_HOST
REDIS_PORT = setup.REDIS_PORT
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = setup.TIME_ZONE

CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('for_parsers', Exchange('for_parsers'), routing_key='for_parsers'),
)
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'
