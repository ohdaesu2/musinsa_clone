from django.db import models

from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.models.enums.boolean_choices import BooleanChoices


class DiscountCoupon(BaseModel):
    user = models.ForeignKey(
        to="member.User",
        related_name="user_in_discount_coupon",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("User")
    )
    brand = models.ForeignKey(
        to="shop.Brand",
        related_name="brand_in_discount_coupon",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Brand")
    )
    discount_rate = models.PositiveIntegerField(default=0, verbose_name=_("Discount Rate"))
    is_enabled = models.CharField(
        max_length=1, choices=BooleanChoices.choices, default=BooleanChoices.FALSE, verbose_name=_("Is Enabled")
    )
    disabled_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Disabled At"))

    class Meta:
        db_table = "discount_coupon"
        verbose_name = _("Discount_Coupon")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ['-id']

    def __str__(self):
        return f"Discount Coupon(pk={self.pk}, name={self.brand})"
