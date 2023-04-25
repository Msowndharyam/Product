# # Import necessary modules
# from celery import shared_task
# from celery.schedules import crontab
# from datetime import timedelta
# from products.models import Product
# from django.conf import settings

# @shared_task
# def update_discounted_prices():
#     products = Product.objects.all()
#     for product in products:
#         discounted_price = product.price * 0.5
#         product.discounted_price = discounted_price
#         product.save()


# CELERY_BEAT_SCHEDULE = {
#     'update-discounted-prices': {
#         'task': 'app.tasks.update_discounted_prices',
#         'schedule': crontab(minute='*/15'),
#     },
# }
