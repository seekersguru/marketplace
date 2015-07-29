# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20150629_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tentative_wedding_date',
            field=models.CharField(default=datetime.date(2015, 7, 21), max_length=20),
            preserve_default=False,
        ),
    ]
