from django.urls import reverse

def menu_items(request):
    menu = [
        {'name': 'О нас', 'url': reverse('about'), 'staff_only': False},
        {'name': 'Каталог игр', 'url': reverse('game_catalog'), 'staff_only': False},
        {'name': 'Аренда', 'url': reverse('rent_catalog'), 'staff_only': False},
        {'name': 'Доставка', 'url': reverse('delivery'), 'staff_only': False},
        {'name': 'Контакты', 'url': reverse('contacts'), 'staff_only': False},
    ]   