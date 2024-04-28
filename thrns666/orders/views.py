from django.http import HttpResponse
from django.shortcuts import render
from marshallite_cart.context_processor import cart_total_amount
from .tasks import order_created
from .models import OrderItem, Order
from marshallite_cart.cart import Cart


def user_orders_list(request):
    if not request.user.id:
        return HttpResponse('Unauthorized', status=401)

    user_orders = Order.objects.filter(user=request.user.id).values()

    return render(request, 'order/user_orders_list_page.html', {'user_orders': user_orders})


def order_create(request):
    if not request.user.id:
        return HttpResponse('Unauthorized', status=401)

    cart = Cart(request)

    if request.method == 'POST':
        order = Order.objects.create(
            user_id=request.user.id,
            order_sum=cart_total_amount(request).get('cart_total_amount')
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        order_created.delay(order.id)
        return render(request, 'order/created.html', {'order': order})
    else:
        return render(request, 'order/create.html', {'cart': cart})
