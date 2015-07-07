# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0002_auto_20150704_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='from_to',
            field=models.CharField(max_length=3, choices=[(b'v2c', b'v2c'), (b'c2v', b'c2v')]),
        ),
    ]
