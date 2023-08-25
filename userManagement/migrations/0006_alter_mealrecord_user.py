# Generated by Django 4.2.4 on 2023-08-25 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userManagement', '0005_alter_mealrecord_breakfast_alter_mealrecord_dinner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealrecord',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]