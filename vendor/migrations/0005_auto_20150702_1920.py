# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_auto_20150702_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='vendor',
            new_name='vendor_type',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='role',
            field=models.CharField(max_length=100, choices=[(b'Admin', b'Admin'), (b'Reception', b'Reception')]),
        ),
    ]
