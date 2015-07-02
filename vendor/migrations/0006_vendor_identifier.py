# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_auto_20150702_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='identifier',
            field=models.CharField(default=datetime.date(2015, 7, 2), max_length=512),
            preserve_default=False,
        ),
    ]
