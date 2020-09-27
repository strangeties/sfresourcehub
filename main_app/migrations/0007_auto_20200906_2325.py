# Generated by Django 3.1 on 2020-09-06 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200906_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='resource',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=12),
        ),
        migrations.AlterField(
            model_name='resource',
            name='long',
            field=models.DecimalField(decimal_places=6, max_digits=12),
        ),
    ]