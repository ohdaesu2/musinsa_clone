from django.db import models


class BooleanChoices(models.TextChoices):
    TRUE = "T", "True"
    FALSE = "F", "False"