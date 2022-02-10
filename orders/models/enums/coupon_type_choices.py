from django.db import models

from django.utils.translation import gettext_lazy as _


class CouponTypeChoices(models.TextChoices):
    PERIOD = "Period", _("Period")
    BRAND = "Brand", _("Brand")
