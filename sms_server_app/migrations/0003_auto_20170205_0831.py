# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_server_app', '0002_auto_20170204_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcetm',
            name='api_key',
            field=models.CharField(null=True, blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='sourcetm',
            name='forbidden_groups',
            field=models.CharField(null=True, blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='sourcetm',
            name='phone_ways',
            field=models.CharField(null=True, blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='sourcetm',
            name='taxophone_ways',
            field=models.CharField(null=True, blank=True, max_length=128),
        ),
    ]
