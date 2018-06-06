# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('phone', models.CharField(unique=True, max_length=128)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SmsTM',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('port', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('api_key', models.CharField(max_length=128)),
                ('sms_text', models.CharField(max_length=256)),
                ('default_send_period', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SourceTM',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('port', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('api_key', models.CharField(max_length=128)),
                ('phone_ways', models.CharField(max_length=128)),
                ('taxophone_ways', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Taxophone',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('phone', models.CharField(unique=True, max_length=128)),
                ('used', models.BooleanField()),
                ('send_after_seconds', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
