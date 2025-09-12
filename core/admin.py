from django.contrib import admin
from .models import Product, Arenda

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
