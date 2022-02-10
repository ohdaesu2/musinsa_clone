from django.db import models

from django.utils.translation import gettext_lazy as _


class LevelChoices(models.TextChoices):
    NOOB = 1, _("Noob")  # 앞에는 DB, 뒤에는 UI
    ROOKIE = 2, _("Rookie")
    MEMBER = 3, _("Member")
    BRONZE = 4, _("Bronze")
    SILVER = 5, _("Silver")
    GOLD = 6, _("Gold")
    PLATINUM = 7, _("Platinum")
    DIAMOND = 8, _("Diamond")
