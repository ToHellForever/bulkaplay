from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, View
from .models import Product, Arenda, News, Order, PlayerRange, Size, PlayerCount, PlayerAge, GameType, AdditionalProducts
from .forms import OrderForm
# ИМПОРТ РАНДОМА 
import random
# JsonResponse
from django.http import JsonResponse, HttpResponse


def process_order_form(request, form):
    if form.is_valid():
        data = form.cleaned_data
        order = Order.objects.create(
            name=data["name"],
            phone=data["phone"],
            order_type=data["order_type"],
            date=data["date"],
            time=data["time"],
            comment=data.get("comment", ""),
        )

        # Сохраняем выбранные товары или аренды
        if data["order_type"] == "buy":
            selected_products = request.POST.getlist("selected_products")
            selected_additional_products = request.POST.getlist("selected_additional_products")
            if selected_products:
                products = Product.objects.filter(id__in=selected_products)
                order.products.set(products)
            if selected_additional_products:
                additional_products = AdditionalProducts.objects.filter(id__in=selected_additional_products)
                order.additional_products.set(additional_products)
        elif data["order_type"] == "rent":
            selected_arenda_id = request.POST.get("rental-type")
            selected_games = request.POST.getlist("selected_games")
            if selected_arenda_id:
                arenda = Arenda.objects.filter(id=selected_arenda_id).first()
                if arenda:
                    order.arenda.set([arenda])
            if selected_games:
                games = Product.objects.filter(id__in=selected_games)
                order.games_for_rent.set(games)
        messages.success(request, "Заказ успешно сохранён!")
        return True
    else:
        messages.error(
            request, "Ошибка при отправке формы. Проверьте введённые данные."
        )
        return False



class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(is_active=True).order_by(
            "-created_at"
        )
        context["arenda"] = Arenda.objects.filter(is_active=True).order_by(
            "-created_at"
        )
        context["additional_products"] = AdditionalProducts.objects.filter(is_active=True).order_by(
            "-created_at"
        )
        context["form"] = OrderForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if process_order_form(request, form):
            return redirect("landing")
        else:
            return redirect("landing")


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(is_active=True).order_by(
            "-created_at"
        )
        context["arenda"] = Arenda.objects.filter(is_active=True).order_by(
            "-created_at"
        )
        context["additional_products"] = AdditionalProducts.objects.filter(is_active=True).order_by(
        "-created_at"
        )
        context["news"] = News.objects.filter(is_active=True).order_by("-created_at")
        context["form"] = OrderForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if process_order_form(request, form):
            return redirect("landing")
        else:
            return redirect("landing")


class GameCatalogView(TemplateView):
    template_name = "game_catalog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(is_active=True)

        # Получаем все возможные значения для фильтров
        sizes = Size.objects.all()
        player_counts = PlayerCount.objects.all()
        player_ages = PlayerAge.objects.all()
        game_types = GameType.objects.all()

        # Обработка поискового запроса
        search_query = self.request.GET.get('search', '')
        if search_query:
            products = products.filter(name__iregex=r'{}'.format(search_query))

        # Обработка фильтров
        if 'size' in self.request.GET and self.request.GET['size']:
            products = products.filter(sizes__id=self.request.GET['size'])

        if 'player_count' in self.request.GET and self.request.GET['player_count']:
            products = products.filter(player_counts__id=self.request.GET['player_count'])

        if 'player_age' in self.request.GET and self.request.GET['player_age']:
            products = products.filter(player_ages__id=self.request.GET['player_age'])

        if 'game_type' in self.request.GET and self.request.GET['game_type']:
            products = products.filter(game_types__id=self.request.GET['game_type'])

        # Обработка сортировки
        sort = self.request.GET.get('sort', '')
        if sort == 'price_asc':
            products = products.order_by('price')
        elif sort == 'price_desc':
            products = products.order_by('-price')
        elif sort == 'name_asc':
            products = products.order_by('name')
        elif sort == 'name_desc':
            products = products.order_by('-name')
        else:
            products = products.order_by('-created_at')

        context["products"] = products
        context["additional_products"] = AdditionalProducts.objects.filter(is_active=True).order_by("-created_at")
        context["arenda"] = Arenda.objects.filter(is_active=True).order_by("-created_at")
        context["form"] = OrderForm()

        # Добавляем значения для фильтров в контекст
        context["sizes"] = sizes
        context["player_counts"] = player_counts
        context["player_ages"] = player_ages
        context["game_types"] = game_types

        return context

        def post(self, request, *args, **kwargs):
            form = OrderForm(request.POST)
            if process_order_form(request, form):
                return redirect("landing")
            else:
                return redirect("landing")


class ProductDetailView(TemplateView):
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = get_object_or_404(Product, pk=kwargs["pk"])
        context["products"] = Product.objects.filter(is_active=True).order_by("-created_at")
        context["additional_products"] = AdditionalProducts.objects.filter(is_active=True).order_by("-created_at")
        context["arenda"] = Arenda.objects.filter(is_active=True).order_by("-created_at")
        context["form"] = OrderForm()
        # Берём 3 случайных товара из базы данных
        all_products = list(Product.objects.exclude(id=context["product"].id).prefetch_related('additional_images'))  # Исключаем текущий продукт
        random_products = random.sample(all_products, min(len(all_products), 3))
        context["random_products"] = random_products
        return context
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if process_order_form(request, form):
            return redirect("landing")
        else:
            return redirect("landing")
        
        
class RentalCatalogView(TemplateView):
    template_name = "rental_catalog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(is_active=True).order_by("-created_at")
        context["arenda"] = Arenda.objects.filter(is_active=True).order_by("-created_at")
        context["additional_products"] = AdditionalProducts.objects.filter(is_active=True).order_by("-created_at")  
        context["news"] = News.objects.filter(is_active=True).order_by("-created_at")
        context["form"] = OrderForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if process_order_form(request, form):
            return redirect("landing")
        else:
            return redirect("landing")

def calculate_games(request):
    guests = int(request.GET.get('guests'))
    try:
        player_range = PlayerRange.objects.filter(min_players__lte=guests, max_players__gte=guests).first()
        
        if player_range is not None:
            data = {'min': player_range.min_game_count, 'max': player_range.max_game_count}
        else:
            data = {'min': None, 'max': None}
            
        return JsonResponse(data)
    
    except Exception as e:
        print(f"Ошибка: {e}")
        return JsonResponse({'error': str(e)}, status=500)
    
    
class AdditionalProductDetailView(TemplateView):
    template_name = "additional_product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["additional_product"] = get_object_or_404(AdditionalProducts, pk=kwargs["pk"])
        context["products"] = Product.objects.filter(is_active=True).order_by("-created_at")
        context["additional_products"] = AdditionalProducts.objects.filter(is_active=True).order_by("-created_at")
        context["arenda"] = Arenda.objects.filter(is_active=True).order_by("-created_at")
        context["form"] = OrderForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if process_order_form(request, form):
            return redirect("landing")
        else:
            return redirect("landing")
