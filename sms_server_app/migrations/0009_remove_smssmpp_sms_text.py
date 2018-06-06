# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_server_app', '0008_smssmpp_sms_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smssmpp',
            name='sms_text',
        ),
    ]
