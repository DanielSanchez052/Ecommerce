import os
from celery import Celery
#from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce.config.local')

app = Celery('Ecommerce')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    #15317554