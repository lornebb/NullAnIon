# Generated by Django 3.1.6 on 2021-03-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20210312_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mix',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]