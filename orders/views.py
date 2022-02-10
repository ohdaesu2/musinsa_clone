from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


# Create your views here.
from django.utils.translation import gettext_lazy as _

from orders.coupon_policy.brand_coupon_type import BrandCouponType
from orders.coupon_policy.period_coupon_type import PeriodCouponType
from orders.models.discount_coupon import DiscountCoupon
from orders.models.order import Order
from orders.models.order_item import OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer
from shop.models.clothes import Clothes


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    lookup_field = 'uid'

    def get_queryset(self):
        return Order.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        # order_id 는 필수값
        order_id = request.data.get("order_id", None)
        order_obj = get_object_or_404(Order, uid=order_id)
        # clothes 를 의미하는 unique_number 은 필수값
        unique_number = request.data.get("unique_number", None)
        clothes_obj = get_object_or_404(Clothes, unique_number=unique_number)
        # order_item 삭제
        if order_obj.order_items.filter(clothes=clothes_obj).exists():
            order_obj.order_items.filter(clothes=clothes_obj).delete()
            order_obj.save()
            return Response({
                "message": "The object item deleted in Order"
            },
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                "message": "Can not find clothes information"
            },
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        order_id = request.data.get("order_id")
        order_obj = get_object_or_404(Order, uid=order_id)
        self.perform_destroy(order_obj)
        return Response(
            {
                "message": "Success Delete Order!",
            },
            status=status.HTTP_204_NO_CONTENT
        )

    @action(methods=["POST"], detail=False)
    def order_sheet(self, request):
        user_obj = request.user
        # order_id 는 필수값
        order_id = request.data.get("order_id", None)
        order_obj = Order.objects.get(uid=order_id)
        # clothes 를 나타내는 unique_number 은 필수값
        unique_number = request.data.get("unique_number", None)
        clothes_obj = Clothes.objects.get(unique_number=unique_number)
        # amount 는 선택값
        amount = int(request.data.get("amount", "1"))
        # discount_coupon 은 선택값
        discount_coupon_id = request.data.get("discount_coupon_id", None)
        try:
            discount_coupon_obj = DiscountCoupon.objects.get(uid=discount_coupon_id)
            # print(discount_coupon_obj)
            if discount_coupon_obj.type == 'Period':
                period_coupon = PeriodCouponType(user_obj=user_obj, discount_coupon_obj=discount_coupon_obj)
                # Period Coupon 이 사용할 수 있는 쿠폰인지 확인
                if period_coupon.is_verified():
                    discount_coupon_obj = discount_coupon_obj
                else:
                    return Response({
                        "message": "This Coupon is not available"
                    },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            elif discount_coupon_obj.type == 'Brand':
                brand_coupon = BrandCouponType(user_obj=user_obj, discount_coupon_obj=discount_coupon_obj)
                # Brand Coupon 이 사용할 수 있는 쿠폰인지 확인
                if brand_coupon.is_verified():
                    # Brand Coupon 과 clothes 의 brand 가 일치하는지 확인
                    if brand_coupon.brand_verified(clothes_obj=clothes_obj):
                        discount_coupon_obj = discount_coupon_obj
                    else:
                        return Response({
                            "message": "This Brand Coupon does not match brand of clothes"
                        },
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response({
                        "message": "This Coupon is not available"
                    },
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except DiscountCoupon.DoesNotExist:
            discount_coupon_obj = None

        with transaction.atomic():
            try:
                print(order_obj)
                print(discount_coupon_obj)
                # 만약 추가하려는 item 이 이미 order 에 이미 담겨 있다면 error 발생
                if order_obj.order_items.filter(clothes=clothes_obj).exists():
                    return Response(
                        {
                            "message": "This item already exists order",
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                else:
                    order_item_obj = OrderItem.objects.create(
                        clothes=clothes_obj,
                        order=order_obj,
                        amount=amount,
                        price=clothes_obj.price,
                        discount_coupon=discount_coupon_obj,
                    )
                    print(order_item_obj)
                    order_obj.save()
            except Exception as e:
                print(e)
                return Response(
                    {
                        "message": "order failed",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if order_item_obj is not None:
            data = {
                "message": "Successful!",
                "order_id": order_id,
                "order_item_unique_number": order_item_obj.clothes.unique_number
            }

            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "order_check_error": _("order_check failed"),
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)