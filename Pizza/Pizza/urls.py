from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('product.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('product/', include('django.contrib.auth.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path(' ', include(('product.urls', 'shop'), namespace='shop')),
    path('orders/', include('orders.urls', namespace='orders')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
