# Generated by Django 3.1.6 on 2021-03-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20210313_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mix',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=22.22, max_digits=10),
        ),
    ]
