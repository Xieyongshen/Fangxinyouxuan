# Generated by Django 2.0.7 on 2018-08-10 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20180810_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproduct',
            name='buyTimes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 10, 11, 8, 28, 424688)),
        ),
    ]
