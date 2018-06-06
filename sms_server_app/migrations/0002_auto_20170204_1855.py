# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_server_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='send_after_seconds',
            field=models.IntegerField(default=36000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='used',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smstm',
            name='send_to_phone_table',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smstm',
            name='send_to_taxophone_table',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sourcetm',
            name='forbidden_groups',
            field=models.CharField(max_length=128, default=''),
            preserve_default=False,
        ),
    ]
