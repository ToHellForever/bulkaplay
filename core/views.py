from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Arenda

def landing(request):
    # Получаем все активные товары для карусели
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    arenda = Arenda.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'landing.html', {'products': products, 'arenda': arenda})
