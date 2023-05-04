# Generated by Django 4.2 on 2023-04-24 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delyzer', '0007_alter_departure_current_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departure',
            name='current_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='departure',
            name='planned_departure_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
