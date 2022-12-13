from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from .forms import ImageForm
from django.shortcuts import render
import random
from django.urls import reverse_lazy
from .models import Product
from cart.forms import CartAddProductForm

def ProductListView(request):
    products = models.Product.objects.all()
    all_ids = []
    cart_product_form = CartAddProductForm()
    errorCheck = 0
    for product in products:
        all_ids.append(product.pk)
    if len(products) >= 3:
        random_f = random.choice(all_ids)
        random_s = random.choice(all_ids)
        while True:
            if random_s != random_f:
                break
            else:
                random_s = random.choice(all_ids)
        random_t = random.choice(all_ids)
        while True:
            if random_t != random_f and random_t != random_s:
                break
            else:
                random_t = random.choice(all_ids)
        return render(request, 'product_list.html', {'product_list':products, 'random_f':random_f, 'random_s':random_s, 'random_t':random_t, 'errorCheck':errorCheck, 'cart_product_form': cart_product_form})
    else:
        errorCheck = 1
        return render(request, 'product_list.html', {'product_list':products, 'errorCheck':errorCheck, 'cart_product_form': cart_product_form})


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_new.html'
    fields = ['name', 'price', 'description', 'weight', 'cm', 'image']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Product
    fields = ['name', 'price', 'description', 'weight', 'cm', 'image']
    template_name = 'product_edit.html'
    login_url = 'login'


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'product_new.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'product_new.html', {'form': form})

