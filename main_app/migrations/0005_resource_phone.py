# Generated by Django 3.0.7 on 2020-08-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200823_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='phone',
            field=models.IntegerField(blank=True, default=123456789),
        ),
    ]
