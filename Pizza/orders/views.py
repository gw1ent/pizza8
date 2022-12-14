from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import OrderItem
from .forms import OrderCreateForm, OrderDetailForm
from cart.cart import Cart
from django.views.generic import ListView
from .models import Order
from . import models

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            o = Order.objects.get(id = order.pk)
            o.user = request.user
            o.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return HttpResponseRedirect(reverse_lazy('product_list'))
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})

def order_detail(request):
    myorders = Order.objects.filter(user=request.user)
    orderitems = []
    for order in myorders:
        orderitems.append(OrderItem.objects.filter(order = order))
        print(OrderItem.objects.filter(order = order))
    if request.method == 'POST':
        form = OrderDetailForm(request.POST)
    else:
        form = OrderDetailForm
    data = {
        'myorders' : myorders,
        'orderitems' : orderitems
    }
    return render(request, 'orders/order/order_detail.html', data)
