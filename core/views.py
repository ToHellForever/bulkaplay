from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Product, Arenda


class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_active=True).order_by('-created_at')
        context['arenda'] = Arenda.objects.filter(is_active=True).order_by('-created_at')
        return context

from .forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)  # Здесь можешь сохранить данные в БД или отправить письмо администратору сайта
            return redirect('landing')
    else:
        form = OrderForm()

    products = Product.objects.filter(is_active=True).order_by('-created_at')
    arenda = Arenda.objects.filter(is_active=True).order_by('-created_at')

    return render(request, 'create_order.html', {'form': form, 'products': products, 'arenda': arenda})


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.filter(is_active=True).order_by('-created_at')
        return context