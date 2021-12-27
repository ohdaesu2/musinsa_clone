# Generated by Django 3.0.14 on 2021-12-26 08:55

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.PositiveIntegerField(choices=[('1', 'Noob'), ('2', 'Rookie'), ('3', 'Member'), ('4', 'Bronze'), ('5', 'Silver'), ('6', 'Gold'), ('7', 'Platinum'), ('8', 'Diamond')], default=1, verbose_name='Level Name')),
                ('discount_rate', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Discount Rate')),
                ('total_point', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Point')),
                ('monthly_discount_coupon_rate', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Monthly Discount Coupon Rate')),
                ('monthly_discount_coupon_count', models.PositiveIntegerField(blank=True, null=True, verbose_name='Monthly Discount Coupon Count')),
            ],
            options={
                'verbose_name': 'User Level',
                'verbose_name_plural': 'User Level List',
                'db_table': 'user_level',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='User Name')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='Name')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Address')),
                ('phone_number', models.CharField(blank=True, max_length=16, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_level', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_level', to='member.UserLevel', verbose_name='User Level')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': '사용자 List',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
