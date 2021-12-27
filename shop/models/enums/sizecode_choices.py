from django.db import models


class SizeCodeChoices(models.TextChoices):
    XS = "XS", "XS"
    S = "S", "S"
    M = "M", "M"
    L = "L", "L"
    XL = "XL", "XL"
    XXL = "2XL", "2XL"
    Free = "F", "Free"
