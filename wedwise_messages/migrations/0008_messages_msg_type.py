# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedwise_messages', '0007_remove_messages_msg_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='msg_type',
            field=models.CharField(default=b'message', max_length=7, choices=[[b'm', b'm'], [b'b', b'b'], [b'b', b'b']]),
            preserve_default=True,
        ),
    ]
