# Generated by Django 2.1.3 on 2018-12-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20181209_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
