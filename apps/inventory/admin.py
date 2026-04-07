from django.contrib import admin
from .models import Inventory, StockMovement


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'minimum_stock', 'is_low_stock')
    search_fields = ('product__name',)

    def is_low_stock(self, obj):
        return obj.quantity <= obj.minimum_stock
    is_low_stock.boolean = True
    is_low_stock.short_description = 'Estoque baixo'


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'movement_type', 'created_at')
    list_filter = ('movement_type',)
    search_fields = ('product__name',)
    ordering = ('-created_at',)