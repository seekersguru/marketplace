# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    replaces = [(b'core', '0001_initial'), (b'core', '0002_vendorfield_fields'), (b'core', '0003_auto_20150524_1344'), (b'core', '0004_vendor_category')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(null=True, upload_to=b'media/vendor_image/', blank=True)),
                ('key', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('length', models.IntegerField()),
                ('value', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('contact_number', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('users', models.ManyToManyField(related_name=b'people', through='core.UserMember', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VendorField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor', models.ForeignKey(related_name=b'membership', to='core.Vendor')),
                ('fields', models.ForeignKey(to='core.Fields', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='usermember',
            name='vendor',
            field=models.ForeignKey(to='core.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vendor',
            name='category',
            field=models.ForeignKey(default=datetime.date(2015, 5, 24), to='core.Category'),
            preserve_default=False,
        ),
    ]
