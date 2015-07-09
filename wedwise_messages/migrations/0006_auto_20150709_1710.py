# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0005_auto_20150709_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='bid_json',
            field=models.CharField(default=None, max_length=1024, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='bid_price',
            field=models.CharField(default=None, max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='bid_quantity',
            field=models.IntegerField(default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='book_json',
            field=models.CharField(default=None, max_length=1024, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='event_date',
            field=models.DateField(default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='status',
            field=models.CharField(default=None, max_length=1, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='time_slot',
            field=models.CharField(default=None, max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
