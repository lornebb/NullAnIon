# Generated by Django 3.1.7 on 2021-03-30 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20210330_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_production',
            name='deliver_by',
            field=models.DateField(),
        ),
    ]
