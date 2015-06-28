# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('key', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to=b'media/vendor_image/')),
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
                ('role', models.CharField(max_length=100, choices=[(b'Owner', b'Owner'), (b'Admin', b'Admin'), (b'Reception', b'Reception')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(to='vendor.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VendorLead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('name', models.CharField(max_length=250)),
                ('contact_number', models.CharField(max_length=20)),
                ('category', models.ForeignKey(to='vendor.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
