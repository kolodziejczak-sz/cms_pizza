# Generated by Django 2.1.3 on 2018-11-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20181129_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navigation',
            options={'ordering': ['sort']},
        ),
        migrations.AlterField(
            model_name='navigation',
            name='sort',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
