from django.db import models

from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class Color(BaseModel):
    name = models.CharField(max_length=10, verbose_name=_("Name"))
    image_url = models.ImageField(upload_to="color/%Y/%m/%d")

    class Meta:
        db_table = "color"
        verbose_name = _("Color")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ['-id']

    def __str__(self):
        return f"Color(pk={self.pk}, name={self.name})"
