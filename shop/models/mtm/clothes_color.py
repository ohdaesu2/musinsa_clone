from django.db import models

from django.utils.translation import gettext_lazy as _

from shop.models.clothes import Clothes
from shop.models.color import Color
from utils.models.base_model import BaseModel


class ClothesColor(BaseModel):
    clothes = models.ForeignKey(
        to="Clothes",
        related_name="clothes_in_clothes_color",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Clothes"),
    )
    color = models.ForeignKey(
        to="Color",
        related_name="color_in_clothes_color",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Color"),
    )

    class Meta:
        db_table = "clothes_color"
        verbose_name = _("Clothes Color")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ["-id"]

    def __str__(self):
        return f"Clothes_Color(pk={self.pk})"
