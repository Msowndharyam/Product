import os

from celery import Celery

from django.conf import settings


# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_example.settings')

# you can change the name here
app = Celery("django_celery_example")

app.conf.update(
    result_backend='db+postgresql://postgres:12345@127.0.0.1:5432/product-celery',
)
# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# discover and load tasks.py from from all registered Django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y

@app.task
def multiply(x, y):
    return x * y

# # Call the task and print its state and result
# task = multiply.delay(3, 4)
# print(task.state)
# print(task.result)