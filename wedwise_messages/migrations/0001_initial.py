# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20150629_1301'),
        ('vendor', '0008_auto_20150704_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_to', models.CharField(max_length=2, choices=[(b'v2c', b'v2c'), (b'c2v', b'c2v')])),
                ('message', models.TextField()),
                ('msg_time', models.DateTimeField()),
                ('event_date', models.DateField()),
                ('quoted_price', models.CharField(max_length=512)),
                ('bid_price', models.FloatField()),
                ('quoted_price_label', models.CharField(max_length=512)),
                ('bid_price_entity', models.FloatField()),
                ('bid_price_entity_label', models.CharField(max_length=512)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('vendor', models.ForeignKey(to='vendor.Vendor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_to', models.CharField(max_length=2, choices=[(b'v2c', b'v2c'), (b'c2v', b'c2v')])),
                ('msg_time', models.DateTimeField()),
                ('quoted_price_label', models.CharField(max_length=512)),
                ('message', models.TextField()),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('vendor', models.ForeignKey(to='vendor.Vendor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_to', models.CharField(max_length=2, choices=[(b'v2c', b'v2c'), (b'c2v', b'c2v')])),
                ('message', models.TextField()),
                ('msg_time', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('vendor', models.ForeignKey(to='vendor.Vendor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
