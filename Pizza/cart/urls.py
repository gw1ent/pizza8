from django.urls import path
from . import views

app_name: 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<product_id>/', views.cart_add, name='cart_add'),
    path('remove/<product_id>/', views.cart_remove, name='cart_remove'),
    path('product-plus/<int:id>/', views.cart_plus_product, name='cart_plus_product'),
    path('product-minus/<int:id>/', views.cart_minus_product, name='cart_minus_product'),
]