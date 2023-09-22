from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from mainsite.models import Product
from .cart import Cart
# from .forms import CartAddProductForm

@login_required(login_url="/login")
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    print(product)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="/users/login")
def item_increment(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    # return redirect("cart_detail")
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="/users/login")
def item_decrement(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login')
def item_clear(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'marshallite_cart/detail.html', {'cart': cart})
