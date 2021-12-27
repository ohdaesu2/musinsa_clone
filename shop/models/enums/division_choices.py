from django.db import models


class DivisionChoices(models.TextChoices):
    OUTER = "O", "Outer"
    TOP = "T", "Top"
    PANTS = "P", "Pants"
    SHOES = "S", "Shoes"
