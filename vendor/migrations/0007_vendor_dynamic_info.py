# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_vendor_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='dynamic_info',
            field=models.TextField(default=datetime.date(2015, 7, 2)),
            preserve_default=False,
        ),
    ]
