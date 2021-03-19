# Generated by Django 3.1.6 on 2021-03-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20210318_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mix',
            options={'verbose_name_plural': 'Mixes'},
        ),
        migrations.AddField(
            model_name='master',
            name='contact',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='mix',
            name='contact',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='production',
            name='contact',
            field=models.EmailField(default='', max_length=254),
        ),
    ]