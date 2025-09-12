from django import forms
from .models import Product, Arenda
from django.utils import timezone
from datetime import datetime

ORDER_TYPES = [
    ('buy', 'Купить'),
    ('rent', 'Аренда')
]


class OrderForm(forms.Form):
    name = forms.CharField(label='Имя:', max_length=100)
    phone = forms.CharField(label='Телефон:', max_length=15)
    order_type = forms.ChoiceField(label='Что вас интересует?', choices=ORDER_TYPES, initial='buy')
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label='Продукты:')
    arenda = forms.ModelMultipleChoiceField(queryset=Arenda.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label='Предметы аренды:')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='Комментарий к заказу:', required=False)