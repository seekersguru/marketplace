# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_vendor_dynamic_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='fbid',
            field=models.CharField(default=b'', max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vendor',
            name='gid',
            field=models.CharField(default=b'', max_length=1024),
            preserve_default=True,
        ),
    ]
