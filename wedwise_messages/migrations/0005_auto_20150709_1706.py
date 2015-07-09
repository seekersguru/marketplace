# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0004_auto_20150709_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='bid_json',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='bid_price',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='bid_quantity',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='book_json',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='status',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='time_slot',
        ),
    ]
