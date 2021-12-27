from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from member.models.user import User
from member.models.user_level import UserLevel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserLevel)
class UserLevelAdmin(admin.ModelAdmin):
    pass
