# Generated by Django 3.2.6 on 2021-08-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='_type',
            field=models.CharField(blank=True, choices=[('Web App', 'Web App'), ('Mobile App', 'Mobile App'), ('Scripting/Bot', 'Scripting/Bot')], max_length=100, null=True),
        ),
    ]
