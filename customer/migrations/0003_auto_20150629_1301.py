# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20150629_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fbid',
            field=models.CharField(default=0, max_length=1024),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gid',
            field=models.CharField(default=0, max_length=1024),
        ),
    ]
