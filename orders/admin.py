from django.contrib import admin

# Register your models here.
from orders.models.discount_coupon import DiscountCoupon
from orders.models.order import Order
from orders.models.order_item import OrderItem
from orders.models.shoppingbag import Shoppingbag


@admin.register(DiscountCoupon)
class DiscountCouponAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Shoppingbag)
class ShoppingbagAdmin(admin.ModelAdmin):
    pass
