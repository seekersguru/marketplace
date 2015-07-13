# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0008_messages_msg_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='bid_json',
            field=models.TextField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='book_json',
            field=models.TextField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='msg_type',
            field=models.CharField(max_length=7, choices=[[b'message', b'message'], [b'bid', b'bid'], [b'book', b'book']]),
        ),
    ]
