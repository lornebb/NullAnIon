# Generated by Django 3.1.6 on 2021-03-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20210311_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='order_type',
            field=models.CharField(default='Master', editable=False, max_length=15),
        ),
        migrations.AlterField(
            model_name='mix',
            name='order_type',
            field=models.CharField(default='Mix', editable=False, max_length=15),
        ),
        migrations.AlterField(
            model_name='production',
            name='order_type',
            field=models.CharField(default='Production', editable=False, max_length=15),
        ),
    ]