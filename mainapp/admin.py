from django.contrib import admin
from .models import ProductCategory, Product


class ProductInline(admin.TabularInline):
    model = Product
    fields = 'name', 'short_desc'
    extra = 1


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = ProductInline,


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = 'is_hot',
    search_fields = 'name',
    list_display = 'name', 'category', 'price', 'is_hot',
    readonly_fields = 'quantity',
