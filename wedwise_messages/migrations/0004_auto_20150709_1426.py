# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0003_auto_20150707_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.RemoveField(
            model_name='book',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='book',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='messages',
            name='bid_json',
            field=models.CharField(default=datetime.date(2015, 7, 9), max_length=1024, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='bid_price',
            field=models.CharField(default=datetime.date(2015, 7, 9), max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='bid_quantity',
            field=models.IntegerField(default=datetime.date(2015, 7, 9), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='book_json',
            field=models.CharField(default=datetime.date(2015, 7, 9), max_length=1024, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='event_date',
            field=models.DateField(default=datetime.date(2015, 7, 9), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='msg_type',
            field=models.CharField(default=datetime.date(2015, 7, 9), max_length=7, choices=[[b'm', b'm'], [b'b', b'b'], [b'b', b'b']]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='status',
            field=models.CharField(default=datetime.date(2015, 7, 9), max_length=1, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='time_slot',
            field=models.CharField(default=datetime.date(2015, 7, 9), max_length=128, blank=True),
            preserve_default=False,
        ),
    ]
