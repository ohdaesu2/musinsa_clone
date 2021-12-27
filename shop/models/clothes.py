from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.models.brand import Brand
from shop.models.guide import Guide
from shop.models.size import Size
from shop.models.color import Color

from utils.models.base_model import BaseModel
from utils.models.enums.boolean_choices import BooleanChoices
from utils.models.enums.gender_choices import GenderChoices


class Clothes(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    price = models.IntegerField(default=0, verbose_name=_("Price"))
    brand = models.ForeignKey(
        to="Brand",
        related_name="brand",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Brand")
    )
    size = models.OneToOneField(
        to="Size",
        related_name="clothes_size",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Size")
    )
    guide = models.OneToOneField(
        to="Guide",
        related_name="clothes_guide",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Guide")
    )
    categories = models.ManyToManyField(
        to="Category",
        through="ClothesCategory",
        blank=True,
        verbose_name=_("Categories")
    )
    color = models.ManyToManyField(
        to="Color",
        through="ClothesColor",
        blank=True,
        verbose_name=_("Color")
    )

    season = models.CharField(max_length=5, blank=True, verbose_name=_("Season"))
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices, verbose_name=_("Gender"))
    unique_number = models.CharField(max_length=50, blank=True, verbose_name=_("Unique Number"))
    amount = models.IntegerField(default=0, verbose_name=_("Amount"))
    image_url = models.ImageField(blank=True, upload_to="clothes/%Y/%m/%d")
    description_url = models.TextField(blank=True, verbose_name=_("Description URL"))
    views_count = models.IntegerField(default=0, verbose_name=_("Views Count"))
    likes_count = models.IntegerField(default=0, verbose_name=_("Likes Count"))
    total_sales = models.IntegerField(default=0, verbose_name=_("Total Sales"))
    is_visualize = models.CharField(
        max_length=1, choices=BooleanChoices.choices, default=BooleanChoices.FALSE, verbose_name=_("Is Visualize")
    )
    is_discount = models.CharField(
        max_length=1, choices=BooleanChoices.choices, default=BooleanChoices.FALSE, verbose_name=_("Is Discount")
    )
    discount_rate = models.IntegerField(default=0, verbose_name=_("Discount Rate"))

    class Meta:
        db_table = "clothes"
        verbose_name = _("Clothes")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ['-id']

    def __str__(self):
        return f"Clothes(pk={self.pk}, name={self.name})"




