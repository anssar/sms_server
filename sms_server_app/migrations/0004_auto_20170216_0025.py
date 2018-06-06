# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_server_app', '0003_auto_20170205_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smstm',
            name='send_to_phone_table',
        ),
        migrations.RemoveField(
            model_name='smstm',
            name='send_to_taxophone_table',
        ),
        migrations.AddField(
            model_name='smstm',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smstm',
            name='phone_prefix',
            field=models.CharField(null=True, max_length=128, blank=True),
        ),
    ]
