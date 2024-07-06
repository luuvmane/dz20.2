from django.contrib import admin
from .models import Product
from .models import BlogPost


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


admin.site.register(BlogPost)