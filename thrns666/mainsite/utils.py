footer_first_col = {'Информация': [{'title': 'Вакансии', 'link': 'works'}, {'title': 'Доставка', 'link': 'deliverely'}, {'title': 'Оплата', 'link': 'payments'}, {'title': 'Прессе', 'link': 'press'}]}
footer_second_col = {'column_name': 'Время работы', 'days': 'Пн-Вс', 'worktime': '8:30 - 22:30', 'break': 'Без перерывов', 'adress': 'Минск, ул.Пушкина, строение 55б'}
footer_third_col = {'Контакты': [{'operator': 'MTC', 'phone': '+375 (12) 3456789'}, {'operator': 'A1', 'phone': '+375 (34) 3456789'}, {'operator': 'Life', 'phone': '+375 (56) 3456789'}]}
footer_fourth_col = {'Мы в сети': [{'icon': 'fa-brands fa-instagram', 'link': '#'}, {'icon': 'fa-brands fa-telegram', 'link': '#'}, {'icon': 'fa-brands fa-viber', 'link': '#'}]}


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['footer_first_col'] = footer_first_col
        context['footer_second_col'] = footer_second_col
        context['footer_third_col'] = footer_third_col
        context['footer_fourth_col'] = footer_fourth_col
        return context
