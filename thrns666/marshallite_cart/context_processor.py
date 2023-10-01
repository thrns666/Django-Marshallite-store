from decimal import Decimal
from .cart import Cart


def cart_total_amount(request):
    cart = Cart(request)
    total_bill = float()

    for item in cart.cart.values():
        total_bill += item['total_price']
    print(round(total_bill, 2), 'PROCESSOR')
    return {'cart_total_bill': round(total_bill, 2)}
