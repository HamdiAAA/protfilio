# Generated by Django 3.2.6 on 2021-08-10 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(default=2021, validators=[django.core.validators.MaxValueValidator(2021), django.core.validators.MinValueValidator(2007)])),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(default=2021, validators=[django.core.validators.MaxValueValidator(2021), django.core.validators.MinValueValidator(2007)])),
            ],
        ),
    ]