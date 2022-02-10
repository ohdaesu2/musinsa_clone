from django.db import models

from django.utils.translation import gettext_lazy as _


class LevelMinimumPoint(models.TextChoices):
    NOOB = 0, "0"  # 앞에는 DB, 뒤에는 UI
    ROOKIE = 2000, "2000"
    MEMBER = 10000, "10000"
    BRONZE = 100000, "100000"
    SILVER = 200000, "200000"
    GOLD = 500000, "500000"
    PLATINUM = 1000000, "1000000"
    DIAMOND = 2000000, "2000000"
