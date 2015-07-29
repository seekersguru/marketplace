# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customer_tentative_wedding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='forgot_code',
            field=models.CharField(max_length=50, null=1),
            preserve_default=True,
        ),
    ]
