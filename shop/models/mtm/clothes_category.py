from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.models.category import Category
from shop.models.clothes import Clothes
from utils.models.base_model import BaseModel


class ClothesCategory(BaseModel):
    clothes = models.ForeignKey(
        to="Clothes",
        related_name="clothes_in_clothes_category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Clothes")
    )
    category = models.ForeignKey(
        to="Category",
        related_name="category_in_clothes_category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Category")
    )

    class Meta:
        db_table = "clothes_category"
        verbose_name = _("Clothes Category")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ['-id']

    def __str__(self):
        return f"Clothes_Category(pk={self.pk})"
