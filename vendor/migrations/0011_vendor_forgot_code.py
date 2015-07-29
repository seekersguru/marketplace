# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0010_remove_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='forgot_code',
            field=models.CharField(max_length=50, null=1),
            preserve_default=True,
        ),
    ]
