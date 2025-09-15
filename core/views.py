from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Product, Arenda, News, Order
from .forms import OrderForm

def process_order_form(request, form):
    if form.is_valid():
        data = form.cleaned_data
        order = Order.objects.create(
            name=data['name'],
            phone=data['phone'],
            order_type=data['order_type'],
            comment=data.get('comment', '')
        )

        # Сохраняем выбранные товары или аренды
        if data['order_type'] == 'buy':
            selected_products = request.POST.getlist('selected_products')
            order.products.set(selected_products)
        elif data['order_type'] == 'rent':
            selected_arenda_id = request.POST.get('rental-type')
            selected_games = request.POST.getlist('selected_games')
            if selected_arenda_id:
                order.arenda.set([selected_arenda_id])
            order.games_for_rent.set(selected_games)
        messages.success(request, "Заказ успешно сохранён!")
        return True
    else:
        messages.error(request, "Ошибка при отправке формы. Проверьте введённые данные.")
        return False

class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_active=True).order_by('-created_at')
        context['arenda'] = Arenda.objects.filter(is_active=True).order_by('-created_at')
        context['form'] = OrderForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if process_order_form(request, form):
            return redirect('landing')
        else:
            return redirect('landing')



class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_active=True).order_by('-created_at')
        context['arenda'] = Arenda.objects.filter(is_active=True).order_by('-created_at')
        context['news'] = News.objects.filter(is_active=True).order_by('-created_at')
        context['form'] = OrderForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if process_order_form(request, form):
            return redirect('landing')
        else:
            return redirect('landing')
