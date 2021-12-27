from django.db import models

from django.utils.translation import gettext_lazy as _


class LevelChoices(models.TextChoices):
    Noob = 1, _("Noob")  # 앞에는 DB, 뒤에는 UI
    Rookie = 2, _("Rookie")
    Member = 3, _("Member")
    Bronze = 4, _("Bronze")
    Silver = 5, _("Silver")
    Gold = 6, _("Gold")
    Platinum = 7, _("Platinum")
    Diamond = 8, _("Diamond")