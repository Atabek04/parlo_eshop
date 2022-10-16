from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from main.views import indexHandler, catalogHandler, catalogItemHandler, goodHandler

urlpatterns = [
    path('', indexHandler, name='index'),
    path('catalog/', catalogHandler, name='catalog'),
    path('catalog/<int:catalog_id>/', catalogItemHandler),
    path('good/<int:good_id>/', goodHandler, name='product-details'),
    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)