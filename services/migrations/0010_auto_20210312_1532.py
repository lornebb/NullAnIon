# Generated by Django 3.1.6 on 2021-03-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20210312_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='reference_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='mix',
            name='reference_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='reference_link',
            field=models.URLField(blank=True),
        ),
    ]
