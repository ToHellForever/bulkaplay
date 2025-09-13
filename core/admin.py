from django.contrib import admin
from .models import Product, Arenda, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    
@admin.register(Arenda)
class ArendaAdmin(admin.ModelAdmin):    
    list_display = ('name', 'price', 'is_active', 'created_at', 'game_count')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'order_type', 'created_at', 'get_products', 'get_games_for_rent')
    list_filter = ('order_type', 'created_at')
    search_fields = ('name', 'phone', 'comment')

    def get_products(self, obj):
        return ", ".join([p.name for p in obj.products.all()])
    get_products.short_description = "Выбранные товары"
    
    def get_games_for_rent(self, obj):
        return ", ".join([g.name for g in obj.games_for_rent.all()])
    get_games_for_rent.short_description = "Игры для аренды"
