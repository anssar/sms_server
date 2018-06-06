# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_server_app', '0005_phone1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='marker',
            field=models.CharField(default='default', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone1602',
            name='marker',
            field=models.CharField(default='default', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sourcetm',
            name='marker',
            field=models.CharField(default='default', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxophone',
            name='marker',
            field=models.CharField(default='default', max_length=128),
            preserve_default=False,
        ),
    ]
