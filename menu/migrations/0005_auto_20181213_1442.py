# Generated by Django 2.1.3 on 2018-12-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menuconfig'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['sort']},
        ),
        migrations.AddField(
            model_name='product',
            name='sort',
            field=models.PositiveIntegerField(default=0),
        ),
    ]