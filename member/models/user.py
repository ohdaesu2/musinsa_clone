from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models.base_model import BaseModel


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=20, unique=True, verbose_name=_("User Name"))
    name = models.CharField(max_length=20, blank=True,  verbose_name=_("Name"))
    address = models.CharField(max_length=100, blank=True, verbose_name=_("Address"))
    phone_number = models.CharField(max_length=16, blank=True, verbose_name=_("Phone Number"))
    email = models.EmailField(blank=False, unique=True, verbose_name=_("Email Address"))
    # total point 로 User Level 결정
    total_point = models.PositiveIntegerField(blank=True, null=True, verbose_name=_("Total Point"))
    user_level = models.OneToOneField(
        to="UserLevel",
        related_name="user_level",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("User Level"),
    )

    # EMAIL_FIELD = "email"
    # REQUIRED_FIELDS = []
    # objects = UserManager()

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ['-id']

    def __str__(self):
        return f"User(pk={self.pk}, username={self.username})"

