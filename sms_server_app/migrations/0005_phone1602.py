# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_server_app', '0004_auto_20170216_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone1602',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(unique=True, max_length=128)),
                ('used', models.BooleanField()),
            ],
        ),
    ]
