# Generated by Django 2.1.3 on 2018-12-12 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_appconfig_currency_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appconfig',
            name='currency_label',
        ),
    ]
