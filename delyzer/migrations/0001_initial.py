# Generated by Django 4.2 on 2023-04-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.CharField(max_length=5)),
                ('line_name', models.CharField(max_length=40)),
                ('planned_departure', models.DateTimeField()),
                ('real_departure', models.DateTimeField()),
                ('delay', models.IntegerField()),
            ],
        ),
    ]
