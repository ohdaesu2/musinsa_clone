# Generated by Django 3.0.14 on 2021-12-27 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0005_modify_category_size_clothes_field_conditions"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscountCoupon",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "discount_rate",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Discount Rate"
                    ),
                ),
                (
                    "is_enabled",
                    models.CharField(
                        choices=[("T", "True"), ("F", "False")],
                        default="F",
                        max_length=1,
                        verbose_name="Is Enabled",
                    ),
                ),
                (
                    "disabled_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Disabled At"),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="brand_in_discount_coupon",
                        to="shop.Brand",
                        verbose_name="Brand",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_in_discount_coupon",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "total_price",
                    models.PositiveIntegerField(default=0, verbose_name="Total Price"),
                ),
                (
                    "consumer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consumer",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Consumer",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ShoppingBag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(default=0, verbose_name="Amount"),
                ),
                (
                    "is_deleted",
                    models.CharField(
                        choices=[("T", "True"), ("F", "False")],
                        default="F",
                        max_length=1,
                        verbose_name="Is Deleted",
                    ),
                ),
                (
                    "clothes",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="clothes_in_shoppingbag",
                        to="shop.Clothes",
                        verbose_name="Clothes",
                    ),
                ),
                (
                    "consumer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consumer_in_shoppingbag",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Consumer",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(default=1, verbose_name="Order Item"),
                ),
                ("price", models.PositiveIntegerField(default=0, verbose_name="Price")),
                (
                    "is_canceled",
                    models.CharField(
                        choices=[("T", "True"), ("F", "False")],
                        default="F",
                        max_length=1,
                        verbose_name="Is Canceled",
                    ),
                ),
                (
                    "clothes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clothes_in_order_item",
                        to="shop.Clothes",
                        verbose_name="Clothes",
                    ),
                ),
                (
                    "discount_coupon",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="discount_coupon_in_order_item",
                        to="orders.DiscountCoupon",
                        verbose_name="Discount Coupon",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="order_in_order_item",
                        to="orders.Order",
                        verbose_name="Order",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
