from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import BaseUserManager


# __는 java의 private 형태를 의미한다.
class UserManager(BaseUserManager):
    def __create_user(self, username, password, **extra_fields):
        if username is None:
            raise TypeError(_("Users must have a username"))

        if password is None:
            raise TypeError(_("User must have a password"))

        username = self.model.normalize_username(username)
        # email = self.model.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self.__create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.__create_user(username, password, **extra_fields)

