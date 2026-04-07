from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)
    list_editable = ('price', 'is_active')
    ordering = ('-created_at',)