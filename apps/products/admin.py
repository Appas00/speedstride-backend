from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'color')
    search_fields = ('name',)
    list_filter = ('color', 'stock')

admin.site.register(Product, ProductAdmin)