# Generated by Django 4.2.4 on 2023-08-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0002_alter_nutritionfacts_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='mealRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('day', models.DateField()),
                ('breakfast', models.TextField()),
                ('lunch', models.TextField()),
                ('dinner', models.TextField()),
                ('snack', models.TextField()),
            ],
        ),
    ]
