from rest_framework import serializers

from orders.models.discount_coupon import DiscountCoupon
from orders.models.order import Order
from orders.models.order_item import OrderItem
from orders.models.shopping_bag import ShoppingBag
from shop.models.clothes import Clothes


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'clothes',
            'price',
            'amount',
            'discount_coupon',
        )


class DiscountCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCoupon
        fields = (
            'discount_rate',
            'is_enabled',
            'disabled_at',
        )


class OrderSerializer(serializers.ModelSerializer):
    # 사실 "get_order_itmes"를 안써줘도 자동으로 완성된다.
    order_items = serializers.SerializerMethodField("get_order_items")
    discount_coupon = DiscountCouponSerializer(required=False)

    class Meta:
        model = Order
        fields = (
            'uid',
            'order_items',
            'discount_coupon',
            'total_price',
            'total_amount',
        )

    @staticmethod
    def get_order_items(instance: Order):
        order_item_objs = instance.order_items.all()
        serializer = OrderItemSerializer(instance=order_item_objs, many=True)
        return serializer.data
