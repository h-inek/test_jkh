import os

from celery import Celery
from celery.worker.state import requests

from test_jkh.settings import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_jkh.settings')

app = Celery('test_jkh')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
BASE_URL = env.str('BASE_URL', 'BASE_URL')


@app.task
def call_rent_for_house_endpoint(house_id, date):
    url = f'{BASE_URL}/api/rent-for-house/'
    data = {
        'house': house_id,
        'date': date
    }
    return requests.post(url, json=data)
