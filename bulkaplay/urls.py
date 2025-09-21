from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from core.views import (
    LandingView, 
    AboutView, 
    GameCatalogView,
    ProductDetailView,
    RentalCatalogView,
    AdditionalProductDetailView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view(), name='landing'),
    path('about/', AboutView.as_view(), name='about'),
    path('game_catalog/', GameCatalogView.as_view(), name='game_catalog'),
    path('game_catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('rental_catalog/', RentalCatalogView.as_view(), name='rental_catalog'),
    path('additional_product_detail/<int:pk>/', AdditionalProductDetailView.as_view(), name='additional_product_detail'),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
