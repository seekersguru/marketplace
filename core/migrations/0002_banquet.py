# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banquet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('plotno', models.IntegerField()),
                ('area', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('pincode', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
