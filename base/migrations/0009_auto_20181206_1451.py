# Generated by Django 2.1.3 on 2018-12-06 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_appconfig'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appconfig',
            old_name='main_color_1',
            new_name='text_color_1',
        ),
        migrations.RenameField(
            model_name='appconfig',
            old_name='main_color_2',
            new_name='text_color_2',
        ),
    ]
