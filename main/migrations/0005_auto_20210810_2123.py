# Generated by Django 3.2.6 on 2021-08-10 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210810_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year',
            field=models.IntegerField(default=2021, validators=[django.core.validators.MinValueValidator(2007)]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='year',
            field=models.IntegerField(default=2021, validators=[django.core.validators.MinValueValidator(2007)]),
        ),
    ]
