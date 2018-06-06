# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_server_app', '0007_auto_20171105_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='smssmpp',
            name='sms_text',
            field=models.CharField(default='test', max_length=256),
            preserve_default=False,
        ),
    ]
