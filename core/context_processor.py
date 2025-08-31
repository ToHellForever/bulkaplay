from django.urls import reverse

def menu_items(request):
    menu = [
        {'name': 'О нас', 'url': reverse('landing'), 'staff_only': False},
        {'name': 'Каталог игр', 'url': reverse('services_views'), 'staff_only': False},
        {'name': 'Аренда', 'url': reverse('order_create'), 'staff_only': False},
        {'name': 'Доставка', 'url': reverse('review_create'), 'staff_only': False},
        {'name': 'Контакты', 'url': reverse('contacts'), 'staff_only': False},
    ]   