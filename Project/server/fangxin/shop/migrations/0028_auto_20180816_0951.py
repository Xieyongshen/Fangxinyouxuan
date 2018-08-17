# Generated by Django 2.0.7 on 2018-08-16 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20180816_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_X',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='纬度'),
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_Y',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='经度'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='limitTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 16, 9, 51, 45, 866947), verbose_name='限时商品截止时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 16, 9, 51, 45, 862929), verbose_name='创建时间'),
        ),
    ]