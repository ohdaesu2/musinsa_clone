import jwt

from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from member.models.user_level import UserLevel
from utils.models.base_model import BaseModel

from member.models.user_manager import UserManager

from datetime import datetime, timedelta


def default_user_level():
    return UserLevel.objects.get(level_name='1')


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=20, unique=True, verbose_name=_("User Name"))
    name = models.CharField(max_length=20, blank=True, verbose_name=_("Name"))
    address = models.CharField(max_length=100, blank=True, verbose_name=_("Address"))
    phone_number = models.CharField(
        max_length=16, blank=True, verbose_name=_("Phone Number")
    )
    email = models.EmailField(blank=False, unique=True, verbose_name=_("Email Address"))
    # total point 로 User Level 결정
    total_point = models.PositiveIntegerField(
        default=0, blank=True, null=True, verbose_name=_("Total Point")
    )
    user_level = models.ForeignKey(
        to="UserLevel",
        default=default_user_level,
        related_name="user_level",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("User Level"),
    )

    USERNAME_FIELD = 'username'
    # 필수값
    REQUIRED_FIELDS = [
        'email'
    ]

    objects = UserManager()

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ["-id"]

    def __str__(self):
        return f"User(pk={self.pk}, username={self.username})"

    def save(self, *args, **kwargs):
        self.user_level = self.__update_user_level()
        return super(User, self).save(*args, **kwargs)

    def __update_user_level(self):
        if self.total_point > int(self.user_level.next_level_minimum_point):
            print(self.user_level.next_level_minimum_point)

            user_level_obj = UserLevel.objects.get(current_level_minimum_point=self.user_level.next_level_minimum_point)
            return user_level_obj

        elif self.total_point < int(self.user_level.current_level_minimum_point):
            user_level_obj = UserLevel.objects.get(next_level_minimum_point=self.user_level.current_level_minimum_point)
            return user_level_obj

        else:
            return self.user_level


