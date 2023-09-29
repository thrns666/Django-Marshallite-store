from decimal import Decimal
from .cart import Cart


def cart_total_amount(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        print(cart)
        for i in cart:
            print(i)
        return sum([item['total_price'] for item in cart])
    else:
        return 0
