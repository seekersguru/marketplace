# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='fbid',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='gid',
            field=models.CharField(default=datetime.date(2015, 6, 29), max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='identifier',
            field=models.CharField(default=2, max_length=512),
            preserve_default=False,
        ),
    ]
