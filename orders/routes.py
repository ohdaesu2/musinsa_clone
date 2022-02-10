from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet

order_router = DefaultRouter()
order_router.register("order", OrderViewSet, basename="order")

urlpatterns = [
    path('', include(order_router.urls))
]
