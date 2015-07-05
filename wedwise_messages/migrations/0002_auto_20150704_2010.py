# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='from_to',
            field=models.CharField(max_length=3, choices=[(b'v2c', b'v2c'), (b'c2v', b'c2v')]),
        ),
    ]
