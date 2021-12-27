from django.db import models

from django.utils.translation import gettext_lazy as _


class LevelMinimumPoint(models.TextChoices):
    Noob = 0, "0"  # 앞에는 DB, 뒤에는 UI
    Rookie = 2000, "2000"
    Member = 10000, "10000"
    Bronze = 100000, "100000"
    Silver = 200000, "200000"
    Gold = 500000, "500000"
    Platinum = 1000000, "1000000"
    Diamond = 2000000, "2000000"
