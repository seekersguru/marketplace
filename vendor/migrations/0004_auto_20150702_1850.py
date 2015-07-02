# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendorlead_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorlead',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
