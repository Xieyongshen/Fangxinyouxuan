# Generated by Django 2.0.7 on 2018-08-20 00:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_auto_20180817_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('del_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('del_name', models.TextField()),
                ('del_freight', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_remain',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='用户余额'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_num',
            field=models.TextField(default='2018082008593348', verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 20, 8, 59, 33, 781988), verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_deliver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Deliver'),
        ),
    ]
