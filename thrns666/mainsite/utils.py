from .models import *


footer = [
    {'Информация': [{'title': 'Вакансии', 'url_name': 'works'}, {'title': 'Доставка', 'url_name': 'deliverely'},{'title': 'Оплата', 'url_name': 'payments'}, {'title': 'Прессе', 'url_name': 'press'}]},
    {'Время работы': ['Пн-Вс', '8:30 - 22:30', 'Без перерывов', 'Минск, ул.Пушкина, строение 55б']},
    {'Контакты': [{'title': 'MTC', '375123456789': '+375 (12) 3456789'}, {'title': 'A1', '375343456789': '+375 (34) 3456789'}, {'title': 'Life', '375563456789': '+375 (56) 3456789'}]},
    {'Мы в сети': [{'icon': 'fa-brands fa-instagram', 'href': '#'},{'icon': 'fa-brands fa-telegram', 'href': '#'}, {'icon': 'fa-brands fa-viber', 'href': '#'}]}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['footer'] = footer
        return context

