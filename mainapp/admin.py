from django.contrib import admin
from .models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProducAdmin(admin.ModelAdmin):
    list_filter = 'is_hot',
    search_fields = 'name',
