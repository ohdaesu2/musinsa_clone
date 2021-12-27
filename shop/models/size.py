from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.models.enums.division_choices import DivisionChoices
from shop.models.enums.sizecode_choices import SizeCodeChoices
from utils.models.base_model import BaseModel


class Size(BaseModel):
    size = models.IntegerField(default=200, blank=True, verbose_name=_("Size"))  # 신발 사이즈
    size_code = models.CharField(
        max_length=3, blank=True, choices=SizeCodeChoices.choices, verbose_name=_("Size Code")
    )  # XS,S,M,L,XL,2XL
    outseam = models.IntegerField(default=0, blank=True, verbose_name=_("Outseam"))  # 바지총장
    shoulder_width = models.IntegerField(default=0, blank=True, verbose_name=_("Shoulder Width"))  # 어깨 너비
    chest_width = models.IntegerField(default=0, blank=True, verbose_name=_("Chest Width"))  # 가슴 너비
    sleeve_length = models.IntegerField(default=0, blank=True, verbose_name=_("Sleeve Length"))  # 소매 길이
    waist_width = models.IntegerField(default=0, blank=True, verbose_name=_("Waist Width"))  # 허리 너비
    thigh_width = models.IntegerField(default=0, blank=True, verbose_name=_("Thigh Width"))  # 허벅지 너비
    rise = models.IntegerField(default=0, blank=True, verbose_name=_("Rise"))  # 밑위
    hem = models.IntegerField(default=0, blank=True, verbose_name=_("Hem"))  # 밑단단면
    clothes_division = models.CharField(
        max_length=1, choices=DivisionChoices.choices, default=DivisionChoices.TOP, verbose_name=_("Clothes Division")
    )  # Outer, TOP, Bottom, Shoes

    class Meta:
        db_table = "size"
        verbose_name = _("Size")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ['-id']

    def __str__(self):
        return f"Size(pk={self.pk}, name={self.clothes_division}, size={self.size_code})"

