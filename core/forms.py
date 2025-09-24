from django import forms
from .models import Product, Arenda, Order
from django.utils import timezone
from datetime import datetime

ORDER_TYPES = [
    ('choice', 'Выбрать...'),
    ('buy', 'Купить игру'),
    ('rent', 'Заказать аренду')
]

class OrderForm(forms.ModelForm):
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

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Дата заказа:',
        initial=datetime.now().strftime('%Y-%m-%d')
    )

    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'step': '60'}),
        label='Время заказа:',
        initial=timezone.now().time()
    )

    class Meta:
        model = Order
        fields = ['name', 'phone', 'order_type', 'date', 'time', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'comment': forms.Textarea(attrs={
                'rows': 1,
                'placeholder': 'Комментарий к заказу...'
            }),
        }
