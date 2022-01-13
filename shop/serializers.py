
from django.db import models

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from shop.models.brand import Brand
from shop.models.category import Category
from shop.models.clothes import Clothes
from shop.models.color import Color
from shop.models.guide import Guide
from shop.models.size import Size


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "name",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
        )


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            "name",
        )


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = (
            "fit",
            "touch",
            "flexibility",
            "see_through",
            "thickness",
            "season",
        )


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            "size",
            "size_code",
            "outseam",
            "shoulder_width",
            "chest_width",
            "sleeve_length",
            "waist_width",
            "thigh_width",
            "rise",
            "hem",
            "clothes_division",
        )


class ClothesSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(required=False)
    guide = GuideSerializer(required=False)
    categories = CategorySerializer(required=False, many=True)
    color = ColorSerializer(required=False, many=True)
    size = SizeSerializer(required=True)

    class Meta:
        model = Clothes
        fields = (
            "name",
            "price",
            "brand",
            "size",
            "guide",
            "categories",
            "color",
            "season",
            "gender",
            "unique_number",
            "amount",
            "image_url",
            "description_url",
            "views_count",
            "likes_count",
            "total_sales",
            "is_visualize",
            "is_discount",
            "discount_rate",
        )

        extra_kwargs = {
            "is_visualize": {
                "read_only": True,
            },
            "is_discount": {
                "read_only": True,
            },
            "discount_rate": {
                "read_only": True,
            }
        }
