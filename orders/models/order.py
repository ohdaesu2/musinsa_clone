import uuid

from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class Order(BaseModel):
    user = models.ForeignKey(
        to="member.User",
        on_delete=models.SET_NULL,
        related_name="user_in_order",
        null=True,
        verbose_name=_("User"),
    )
    uid = models.UUIDField(editable=False, default=uuid.uuid4, verbose_name=_("UID"))
    recipient_name = models.CharField(max_length=30, blank=True, verbose_name=_("recipient_name"))
    delivery_address = models.CharField(max_length=100, blank=True, verbose_name=_("Delivery Address"))
    delivery_memo = models.CharField(max_length=100, blank=True, verbose_name=_("Delivery Memo"))
    phone_number = models.CharField(
        max_length=16, blank=True, verbose_name=_("Phone Number")
    )
    total_price = models.PositiveIntegerField(default=0, verbose_name=_("Total Price"))
    total_amount = models.PositiveIntegerField(default=0, verbose_name=_("Total Amount"))

    class Meta:
        db_table = "order"
        verbose_name = _("Order")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ["-id"]

    def __str__(self):
        return f"Order(uuid={self.uid}, user={self.user})"

    def save(self, *args, **kwargs):
        self.total_price = self.__calculate_total_price()
        self.total_amount = self.__calculate_total_amount()
        return super().save(*args, **kwargs)

    def __calculate_total_price(self):
        if not self.order_items.all().exists():
            return 0
        return self.order_items.aggregate(Sum('price'))['price__sum']

    def __calculate_total_amount(self):
        if not self.order_items.all().exists():
            return 0
        return self.order_items.aggregate(Sum('amount'))['amount__sum']