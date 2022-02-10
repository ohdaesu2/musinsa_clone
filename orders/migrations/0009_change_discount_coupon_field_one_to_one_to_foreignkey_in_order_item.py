# Generated by Django 3.0.14 on 2022-02-10 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_discountcoupon_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='discount_coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discount_coupon_in_order_item', to='orders.DiscountCoupon', verbose_name='Discount Coupon'),
        ),
    ]
