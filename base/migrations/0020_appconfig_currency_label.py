# Generated by Django 2.1.3 on 2018-12-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_auto_20181212_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfig',
            name='currency_label',
            field=models.CharField(default='$', max_length=10),
        ),
    ]
