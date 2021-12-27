from django.contrib import admin

# Register your models here.
from shop.models.brand import Brand
from shop.models.clothes import Clothes
from shop.models.color import Color
from shop.models.guide import Guide
from shop.models.size import Size


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass

