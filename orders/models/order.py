from django.db import models

from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class Order(BaseModel):
    consumer = models.OneToOneField(
        to="member.User",
        related_name="consumer",
        on_delete=models.CASCADE,
        verbose_name=_("Consumer")
    )
    total_price = models.PositiveIntegerField(default=0, verbose_name=_("Total Price"))

    class Meta:
        db_table = "order"
        verbose_name = _("Order")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ['-id']

    def __str__(self):
        return f"Order(pk={self.pk}, name={self.total_price})"