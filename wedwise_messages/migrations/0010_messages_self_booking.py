# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0009_auto_20150713_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='self_booking',
            field=models.CharField(default=None, max_length=1, blank=True),
            preserve_default=True,
        ),
    ]
