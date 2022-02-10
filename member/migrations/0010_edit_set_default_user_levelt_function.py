# Generated by Django 3.0.14 on 2022-01-18 06:05

from django.db import migrations, models
import django.db.models.deletion
import member.models.user


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_change_level_name_in_user_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.ForeignKey(default=member.models.user.default_user_level, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_level', to='member.UserLevel', verbose_name='User Level'),
        ),
    ]
