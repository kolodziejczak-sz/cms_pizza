# Generated by Django 2.1.3 on 2018-12-12 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20181212_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='currency',
        ),
    ]