from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("Name"))

    class Meta:
        db_table = "brand"
        verbose_name = _("Brand")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ["-id"]

    def __str__(self):
        return f"Brand(pk={self.pk}, name={self.name})"
