# Generated by Django 2.1.3 on 2018-12-09 11:34

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20181208_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfig',
            name='accent_color_3',
            field=colorful.fields.RGBColorField(default='#FFFFFF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appconfig',
            name='favicon',
            field=models.ImageField(blank=True, upload_to='config'),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='background_image',
            field=models.ImageField(blank=True, upload_to='config'),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='logo_image',
            field=models.ImageField(blank=True, upload_to='config'),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='subsite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='subsite.Subsite'),
        ),
    ]
