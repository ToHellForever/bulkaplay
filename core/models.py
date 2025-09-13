from django.db import models

class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Arenda(models.Model):
    """Модель аренды"""
    name = models.CharField(max_length=200, verbose_name="Название аренды")
    game_count = models.PositiveIntegerField(verbose_name="Количество игр в аренде", default=6)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Аренда"
        verbose_name_plural = "Аренды"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.game_count} игр)"


class Order(models.Model):
    """Модель заказа"""
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    order_type = models.CharField(max_length=10, choices=[('buy', 'Купить'), ('rent', 'Аренда')], verbose_name="Тип заказа")
    products = models.ManyToManyField(Product, blank=True, verbose_name="Выбранные товары", related_name="order_products")
    arenda = models.ManyToManyField(Arenda, blank=True, verbose_name="Выбранные аренды", related_name="order_arenda")
    games_for_rent = models.ManyToManyField(Product, blank=True, verbose_name="Игры для аренды", related_name="order_games_for_rent")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ от {self.name} ({self.created_at})"

class News(models.Model):
    """Модель новости"""
    name = models.CharField(max_length=200, verbose_name="Название мероприятия")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='news/', verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    date_event = models.DateField(verbose_name="Дата мероприятия")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    def __str__(self):
        return self.name
