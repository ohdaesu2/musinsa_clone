from django.db import models

from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.models.enums.boolean_choices import BooleanChoices


class OrderItem(BaseModel):
    clothes = models.ForeignKey(
        to="shop.Clothes",
        related_name="clothes_in_order_items",
        on_delete=models.CASCADE,
        verbose_name=_("Clothes"),
    )
    order = models.ForeignKey(
        to="Order",
        related_name="order_items",
        on_delete=models.CASCADE,
        verbose_name=_("Order"),
    )
    discount_coupon = models.ForeignKey(
        to="DiscountCoupon",
        related_name="discount_coupon_in_order_item",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Discount Coupon"),
    )
    amount = models.PositiveIntegerField(default=1, verbose_name=_("Amount"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("Price"))
    is_canceled = models.CharField(
        max_length=1,
        choices=BooleanChoices.choices,
        default=BooleanChoices.FALSE,
        verbose_name=_("Is Canceled"),
    )

    class Meta:
        db_table = "order_item"
        verbose_name = _("Order_Item")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ["-id"]

    def __str__(self):
        return f"Order Item(order={self.order}, name={self.clothes})"

    def save(self, *args, **kwargs):
        self.price = self.__calculate_price()
        return super().save(*args, **kwargs)

    def __calculate_price(self):
        cost = self.clothes.price * self.amount
        if self.discount_coupon is None:
            return cost
        else:
            return cost * (1-(self.discount_coupon.discount_rate/100))
