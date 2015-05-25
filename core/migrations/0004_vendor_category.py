# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150524_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='category',
            field=models.ForeignKey(default=datetime.date(2015, 5, 24), to='core.Category'),
            preserve_default=False,
        ),
    ]
