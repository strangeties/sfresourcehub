# Generated by Django 3.0.7 on 2020-09-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='phone',
            field=models.CharField(max_length=32),
        ),
    ]
