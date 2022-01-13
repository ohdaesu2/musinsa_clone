from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.views import ClothesViewSet

shop_router = DefaultRouter()
shop_router.register("clothes", ClothesViewSet)

urlpatterns = [
    path('', include(shop_router.urls))
]