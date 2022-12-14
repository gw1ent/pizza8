from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Product
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product,
                 quantity = 1,
                 update_quantity = cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_plus_product(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.product_plus(product)
    return redirect('cart:cart_detail')


def cart_minus_product(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.product_minus(product)
    return redirect('cart:cart_detail')