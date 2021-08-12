# Generated by Django 3.2.6 on 2021-08-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='_type',
            field=models.CharField(blank=True, choices=[('Technology', 'Technology'), ('Social life', ''), ('Gaming', 'Gaming')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
