import re

from django.contrib.auth import authenticate
from django.db import models

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from member.models.user import User
from member.models.user_level import UserLevel


class UserLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = (
            "level_name",
            "discount_rate",
            "current_level_minimum_point",
            "next_level_minimum_point",
            "monthly_discount_coupon_rate",
            "monthly_discount_coupon_count",
        )

        # extra_kwargs = {
        #     # "discount_rate": {
        #     #     "write_only": True,
        #     # },
        #     # "current_level_minimum_point": {
        #     #     "write_only": True,
        #     # },
        #     # "next_level_minimum_point": {
        #     #     "write_only": True,
        #     # },
        #     "monthly_discount_coupon_rate": {
        #         "read_only": True,
        #     },
        #     "monthly_discount_coupon_count": {
        #         "read_only": True,
        #     }
        # }


class UserSerializer(serializers.ModelSerializer):
    user_level = UserLevelSerializer(required=False)
    password = models.CharField(max_length=128, verbose_name=_("Password"))

    def create(self, validated_data):
        user_obj = User.objects.create(**validated_data)
        password = validated_data.get("password", None)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def validate_phone_number(self, value):
        valid_format = r"^01\d-{0,1}\d{3,4}-{0,1}\d{4}$"
        error_message = _("Valid phone number format: 010-1234-5678 or 01012345678")

        if not value == "" and not bool(re.match(valid_format, value)):
            raise serializers.ValidationError(error_message)

        if "-" in value:
            count = 0
            for letter in value:
                if letter == "-":
                    count += 1
            if count != 2:
                raise serializers.ValidationError(error_message)
            value = value.replace("-", "")

        return value

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "name",
            "address",
            "phone_number",
            "email",
            "total_point",
            "user_level",
        )

        extra_kwargs = {
            "password": {
                "write_only": True,
            },
            # "total_point": {
            #     "read_only": True,
            # },
            # "user_level": {
            #     "read_only": True,
            # }

        }


class ChangePasswordSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    new_password = serializers.CharField(max_length=128)

    def update(self, instance: User, validated_data: dict):
        new_password = validated_data['new_password']
        instance.set_password(new_password)
        instance.save()

        return instance
