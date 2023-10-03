from celery import current_task
from django.core.mail import send_mail
from .models import Order
