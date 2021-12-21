from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Product, ProductAdmin)
