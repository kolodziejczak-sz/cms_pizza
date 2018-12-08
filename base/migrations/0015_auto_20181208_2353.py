# Generated by Django 2.1.3 on 2018-12-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20181206_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appconfig',
            name='baner_image',
        ),
        migrations.RemoveField(
            model_name='appconfig',
            name='baner_text',
        ),
        migrations.AddField(
            model_name='appconfig',
            name='background_image',
            field=models.ImageField(blank=True, upload_to='media/config'),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='logo_image',
            field=models.ImageField(blank=True, upload_to='media/config'),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='logo_text',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
