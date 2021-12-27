from django.db import models
from django.utils.translation import gettext_lazy as _

from member.models.enums.level_choices import LevelChoices
from member.models.enums.level_minimum_point import LevelMinimumPoint


class UserLevel(models.Model):
    level_name = models.PositiveIntegerField(
        default=LevelChoices.Noob, choices=LevelChoices.choices, verbose_name=_("Level Name")
    )
    discount_rate = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_("Discount Rate"))
    current_level_minimum_point = models.PositiveIntegerField(
        choices=LevelMinimumPoint.choices, default=LevelMinimumPoint.Noob, verbose_name=_("Current Level Minimum Point")
    )
    next_level_minimum_point = models.PositiveIntegerField(
        choices=LevelMinimumPoint.choices, default=LevelMinimumPoint.Rookie, verbose_name=_("Next Level Minimum Point")
    )
    monthly_discount_coupon_rate = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name=_("Monthly Discount Coupon Rate")
    )
    monthly_discount_coupon_count = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_("Monthly Discount Coupon Count")
    )

    class Meta:
        db_table = "user_level"
        verbose_name = _("User Level")
        verbose_name_plural = f'{verbose_name} {_("List")}'

    def __str__(self):
        return f"User Lv({self.level_name})"
