from thrns666.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'{order_id}'
    message = f'Ваш заказ был успешно оформлен, ждем вас еще{order.first_name}, номер вашего заказа: {order_id}.'

    mail_send = send_mail(subject, message, 'marshallite@mainsite.ru', [order.email])
    return mail_send
