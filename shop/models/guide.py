from django.db import models

from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class Guide(BaseModel):
    fit = models.CharField(max_length=10, blank=True, verbose_name=_("Fit"))  # 핏
    touch = models.CharField(max_length=10, blank=True, verbose_name=_("Touch"))  # 촉감
    flexibility = models.CharField(
        max_length=10, blank=True, verbose_name=_("Flexibility")
    )  # 신축성
    see_through = models.CharField(
        max_length=10, blank=True, verbose_name=_("See Through")
    )  # 비침
    thickness = models.CharField(
        max_length=10, blank=True, verbose_name=_("Thickness")
    )  # 두께
    Season = models.CharField(max_length=10, blank=True, verbose_name=_("Season"))  # 시즌

    class Meta:
        db_table = "clothes_guide"
        verbose_name = _("Clothes Guide")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ["-id"]

    def __str__(self):
        return f"Guide (pk={self.pk})"
