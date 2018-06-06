# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_server_app', '0006_auto_20170224_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsSmpp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('login', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('sender', models.CharField(max_length=128)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='phone',
            name='smpp_used',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone1602',
            name='smpp_used',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxophone',
            name='smpp_used',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
