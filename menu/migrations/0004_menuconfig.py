# Generated by Django 2.1.3 on 2018-12-12 20:28

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_price_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_label', models.CharField(default='$', max_length=10)),
                ('menu_header', tinymce.models.HTMLField()),
                ('menu_footer', tinymce.models.HTMLField()),
            ],
        ),
    ]