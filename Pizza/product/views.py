from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from .forms import ImageForm
from django.shortcuts import render
import random

def ProductListView(request):
    products = models.Product.objects.all()
    random_f = random.randint(1, len(models.Product.objects.all()))
    random_s = random.randint(1, len(models.Product.objects.all()))
    while True:
        if random_s != random_f:
            break
        else:
            random_s = random.randint(1, len(models.Product.objects.all()))
    random_t = random.randint(1, len(models.Product.objects.all()))
    while True:
        if random_t != random_f and random_t != random_s:
            break
        else:
            random_t = random.randint(1, len(models.Product.objects.all()))
    return render(request, 'product_list.html', {'product_list':products, 'random_f':random_f, 'random_s':random_s, 'random_t':random_t})
class HomePageView(TemplateView):
    template_name="home.html"

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_new.html'
    fields = ['title','body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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

