# Generated by Django 3.2.6 on 2021-08-12 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210812_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='_type',
            field=models.CharField(blank=True, choices=[('Technology', 'Technology'), ('Social life', 'Social life'), ('Gaming', 'Gaming')], max_length=100, null=True),
        ),
    ]