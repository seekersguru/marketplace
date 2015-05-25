# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0004_vendor_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='category',
            field=models.ForeignKey(blank=True, to='core.Category', null=True),
        ),
    ]
