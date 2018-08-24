# Generated by Django 2.0.7 on 2018-08-21 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_auto_20180821_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopproduct',
            old_name='shops',
            new_name='shop',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_num',
            field=models.TextField(default='2018082119531017', verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 21, 19, 53, 10, 431928), verbose_name='创建时间'),
        ),
    ]