# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorlead',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vendorlead',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='vendorlead',
            name='name',
        ),
        migrations.AddField(
            model_name='vendorlead',
            name='address',
            field=models.CharField(default=datetime.date(2015, 7, 2), max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendorlead',
            name='mobile',
            field=models.CharField(default=datetime.date(2015, 7, 2), max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendorlead',
            name='services',
            field=models.CharField(default=datetime.date(2015, 7, 2), max_length=512),
            preserve_default=False,
        ),
    ]
