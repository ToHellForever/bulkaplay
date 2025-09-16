from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=100, verbose_name="Размер")

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return self.name

class PlayerCount(models.Model):
    count = models.PositiveIntegerField(verbose_name="Количество игроков")

    class Meta:
        verbose_name = "Количество игроков"
        verbose_name_plural = "Количество игроков"

    def __str__(self):
        return str(self.count)

class GameType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Вид игры")

    class Meta:
        verbose_name = "Вид игры"
        verbose_name_plural = "Виды игр"

    def __str__(self):
        return self.name

class PlayerAge(models.Model):
    age = models.CharField(max_length=50, verbose_name="Возраст игроков")

    class Meta:
        verbose_name = "Возраст игрока"
        verbose_name_plural = "Возрасты игроков"

    def __str__(self):
        return self.age

class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    # Комплект игры как список строк
    game_kit = models.TextField(verbose_name="Комплект игры", blank=True, null=True)

    # Правила игры
    game_rules = models.TextField(verbose_name="Правила игры", blank=True, null=True)

    # Дополнительная информация
    additional_info = models.TextField(verbose_name="Дополнительно", blank=True, null=True)

    # Связи с атрибутами
    sizes = models.ManyToManyField(Size, verbose_name="Размеры", blank=True)
    player_counts = models.ManyToManyField(PlayerCount, verbose_name="Количество игроков", blank=True)
    game_types = models.ManyToManyField(GameType, verbose_name="Виды игры", blank=True)
    player_ages = models.ManyToManyField(PlayerAge, verbose_name="Возрасты игроков", blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='additional_images',
        verbose_name="Товар",
    )
    image = models.ImageField(upload_to='product_images/additional/', verbose_name="Дополнительное изображение")
    is_main = models.BooleanField(default=False, verbose_name="Основное изображение")

    class Meta:
        verbose_name = "Дополнительное изображение товара"
        verbose_name_plural = "Дополнительные изображения товаров"

    def __str__(self):
        return f'Фото {self.product}'

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

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.name
