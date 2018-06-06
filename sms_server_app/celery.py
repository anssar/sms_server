from __future__ import absolute_import

import os
import random
import json
import time

from celery import Celery
from django.conf import settings

from datetime import datetime, timedelta

from django.utils import timezone

from .models import SourceTM, SmsTM, Phone, Taxophone, Phone1602, SmsSmpp

from .taximaster.api import get_current_orders, send_sms
from .utils import check_phone, send_xml

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms_server.settings')

app = Celery('sms_server')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)    
def debug(self):
    print('OK')

@app.task(bind=True)    
def grab_orders(self):
    source = SourceTM.objects.get(name='Main')
    sms_phone = SmsTM.objects.get(name='Main_phone')
    sms_taxophone = SmsTM.objects.get(name='Main_taxophone')
    to_phone = [str.strip(x) for x in source.phone_ways.split(',')]
    to_taxophone = [str.strip(x) for x in source.taxophone_ways.split(',')]
    try:
        forbidden_groups = [int(str.strip(x)) for x in source.forbidden_groups.split(',')]
    except ValueError:
        forbidden_groups = []
    orders = get_current_orders(source.address, source.port, source.api_key)
    if orders['code'] != 0:
        return
    for order in orders['data']['orders']:
        if not check_phone(order['phone']):
            continue
        if order['order_crew_group_id'] in forbidden_groups:
            continue
        if order['creation_way'] in to_phone:
            try:
                phone = Phone.objects.get(phone=order['phone'])
            except:
                phone = Phone(phone=order['phone'], date=timezone.now(), used=False, smpp_used=False,
                send_after_seconds=sms_phone.default_send_period, marker=source.marker)
                phone.save()
        if order['creation_way'] in to_taxophone:
            try:
                taxophone = Taxophone.objects.get(phone=order['phone'])
            except:
                taxophone = Taxophone(phone=order['phone'], date=timezone.now(), used=False, smpp_used=False,
                send_after_seconds=sms_taxophone.default_send_period, marker=source.marker)
                taxophone.save()

@app.task(bind=True)            
def filter_phones(self):
    taxophones = Taxophone.objects.all()
    phones = Phone.objects.all()
    for phone in taxophones:
        if not check_phone(phone.phone):
            try:
                phone.delete()
            except:
                pass
    for phone in phones:
        if not check_phone(phone.phone):
            try:
                phone.delete()
            except:
                pass
                
@app.task(bind=True)            
def send_sms_task(self, *args, **kwargs):
    models = {'phone': Phone, 'taxophone': Taxophone, 'phone1602': Phone1602}
    count = int(kwargs.get('count', '') or '1')
    interval = int(kwargs.get('interval', '') or '60')
    marker = kwargs.get('marker', '') or 'default'
    sms_tm = kwargs.get('sms_tm', '') or 'Main_taxophone'
    check_used = bool(json.loads(kwargs.get('check_used', '') or 'true'))
    check_marker = bool(json.loads(kwargs.get('check_marker', '') or 'false'))
    model = models.get(kwargs.get('model', '') or 'taxophone', '') or Taxophone
    print("ARGS:{},{};TIME:{}".format(kwargs.get('model', 'taxophone'), sms_tm, timezone.now()))
    try:
        sms_tm = SmsTM.objects.get(name=sms_tm)
    except:
        print('SMS TM NOT FOUND')
        return
    phones = ((model.objects.filter(used=False, marker=marker) if check_marker else model.objects.filter(used=False))
    if check_used else (model.objects.filter(marker=marker) if check_marker else model.objects.all()))
    for i in range(count):
        if sms_tm.active and len(phones) > 0:
            phone = phones[random.randrange(len(phones))]
            print("send to {}({}/{})".format(phone.phone, i+1, count))
            send_sms(sms_tm.address, sms_tm.port, sms_tm.api_key,
            sms_tm.phone_prefix + phone.phone, sms_tm.sms_text)
            phone.used = True
            try:
                phone.save()
            except:
                print('PHONE USED EXCEPT')
        time.sleep(interval)


@app.task(bind=True)            
def send_sms_direct_task(self, *args, **kwargs):
    models = {'phone': Phone, 'taxophone': Taxophone, 'phone1602': Phone1602}
    count = int(kwargs.get('count', '') or '1')
    interval = int(kwargs.get('interval', '') or '60')
    model = models.get(kwargs.get('model', '') or 'taxophone', '') or Taxophone
    sms_smpp_name = kwargs.get('sms_smpp', 'Main') or 'Main'
    sms_text = kwargs.get('sms_text', '')
    print("ARGS:{};TIME:{}".format(kwargs.get('model', 'taxophone'), timezone.now()))
    try:
        sms_smpp = SmsSmpp.objects.get(name=sms_smpp_name)
    except:
        print('SMS SMPP NOT FOUND')
        return
    phones = model.objects.filter(smpp_used=False)
    for i in range(count):
        if sms_smpp.active and len(phones) > 0:
            phone = phones[random.randrange(len(phones))]
            print("send to {}({}/{})".format(phone.phone, i+1, count))
            send_xml(sms_smpp.url, sms_smpp.login, sms_smpp.password,
            sms_smpp.sender, phone.phone, sms_text)
            phone.smpp_used = True
            try:
                phone.save()
            except:
                print('PHONE USED EXCEPT')
        time.sleep(interval)
