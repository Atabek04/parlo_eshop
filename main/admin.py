from atexit import register
from statistics import mode
from django.contrib import admin
from main.models import *



class SingleModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Color, SingleModelAdmin)
admin.site.register(Size, SingleModelAdmin)
admin.site.register(Tag, SingleModelAdmin)
admin.site.register(Category, SingleModelAdmin)
admin.site.register(Good, SingleModelAdmin)
admin.site.register(CategoryBrand, SingleModelAdmin)
admin.site.register(Cart, SingleModelAdmin)
admin.site.register(CartItem, SingleModelAdmin)