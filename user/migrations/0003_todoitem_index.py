# Generated by Django 3.0.8 on 2020-07-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200716_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='index',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
