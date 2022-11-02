from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from main.views import *

urlpatterns = [
    path('', indexHandler, name='index'),
    path('catalog/', catalogHandler, name='catalog'),
    path('catalog/<int:catalog_id>/', catalogItemHandler),
    path('good/<int:good_id>/', goodHandler, name='product-details'),  
    path('cart/', cartHandler, name = 'cart'),
    path('checkout/', checkoutHandler , name='checkout' ),
    path('checkout/success/', checkoutSuccessHandler , name='checkout_success' ),
    path('orders/', ordersHandler, name='orders'),
    path('orders/<int:order_id>/', ordersItemHandler),
    path('compare/', compareHandler, name='compare'),
    path('wishlist/', wishlistHandler, name='wishlist'),
    path('search/', searchHandler),



    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)