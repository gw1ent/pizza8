from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

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
