from django import forms
from .models import Product, Arenda
from django.utils import timezone
from datetime import datetime

ORDER_TYPES = [
    ('choice', 'Выбрать...'),
    ('buy', 'Купить игру'),
    ('rent', 'Заказать аренду')
]


class OrderForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'})
    )
    order_type = forms.ChoiceField(
        label='Что вас интересует?',
        choices=ORDER_TYPES,
        initial='choice'
    )
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Продукты:'
    )
    arenda = forms.ModelMultipleChoiceField(
        queryset=Arenda.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Предметы аренды:'
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 1,
            'placeholder': 'Комментарий к заказу...'
        }),
        label='Комментарий к заказу:',
        required=False
    )