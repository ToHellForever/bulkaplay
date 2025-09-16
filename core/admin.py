from django.contrib import admin
from .models import (
    Product, Arenda, Order, News, ProductImage,
    Size, PlayerCount, GameType, PlayerAge
)
admin.site.register(ProductImage)
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Количество дополнительных форм для новых изображений

# Основной класс для регистрации модели Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    filter_horizontal = ('sizes', 'player_counts', 'game_types', 'player_ages')

    fieldsets = (
        ("Основные поля", {
            'fields': ('name', 'description', 'price', 'image'),
        }),
        ("Атрибуты", {
            'fields': ('sizes', 'player_counts', 'game_types', 'player_ages', 'game_kit', 'game_rules', 'additional_info'),
        }),
        ("Дополнительно", {
            'fields': ('is_active',),
        })
    )

    # Указываем созданный inline-класс
    inlines = [
        ProductImageInline,
    ]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PlayerCount)
class PlayerCountAdmin(admin.ModelAdmin):
    list_display = ('count',)
    search_fields = ('count',)

@admin.register(GameType)
class GameTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PlayerAge)
class PlayerAgeAdmin(admin.ModelAdmin):
    list_display = ('age',)
    search_fields = ('age',)
    
    
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


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_event', 'is_active', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'date_event')
    search_fields = ('name', 'description')
