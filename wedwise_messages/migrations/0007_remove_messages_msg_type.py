# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0006_auto_20150709_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='msg_type',
        ),
    ]
