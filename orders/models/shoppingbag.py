from django.db import models

from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.models.enums.boolean_choices import BooleanChoices


class Shoppingbag(BaseModel):
    clothes = models.ForeignKey(
        to="shop.Clothes",
        related_name="clothes_in_shoppingbag",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Clothes")
    )
    consumer = models.OneToOneField(
        to="member.User",
        related_name="consumer_in_shoppingbag",
        on_delete=models.CASCADE,
        verbose_name=_("Consumer")
    )

    amount = models.PositiveIntegerField(default=0, verbose_name=_("Amount"))
    is_deleted = models.CharField(
        max_length=1, choices=BooleanChoices.choices, default=BooleanChoices.FALSE, verbose_name=_("Is Deleted")
    )

    class Meta:
        db_table = "shoppingbag"
        verbose_name = _("Shoppingbag")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ['-id']

    def __str__(self):
        return f"Shopping Bag(pk={self.pk}, consumer={self.consumer})"