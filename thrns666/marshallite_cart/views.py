from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from mainsite.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@login_required(login_url="/login")
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm(require_POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            action=cd['update']
        )

    return redirect('marshallite_cart:cart_detail')
    # return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login')
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('marshallite_cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'marshallite_cart/detail.html', {'cart': cart})
