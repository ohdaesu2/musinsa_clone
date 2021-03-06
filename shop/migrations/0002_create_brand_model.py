# Generated by Django 3.0.14 on 2021-12-27 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_create_clothes_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                (
                    "clothes",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="brand",
                        to="shop.Clothes",
                        verbose_name="Clothes",
                    ),
                ),
            ],
            options={
                "verbose_name": "Brand",
                "verbose_name_plural": "Brand List",
                "db_table": "brand",
                "ordering": ["-id"],
            },
        ),
    ]
