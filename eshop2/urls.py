from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from main.views import *

urlpatterns = [
    path('', indexHandler, name='index'),
    path('catalog/', catalogHandler, name='catalog'),
    path('catalog/<int:catalog_id>/', catalogItemHandler),
    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)