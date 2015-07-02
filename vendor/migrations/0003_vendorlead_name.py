# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20150702_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorlead',
            name='name',
            field=models.CharField(default=datetime.date(2015, 7, 2), max_length=11),
            preserve_default=False,
        ),
    ]
