# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_auto_20150704_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='email',
        ),
    ]
