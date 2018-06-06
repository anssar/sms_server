from datetime import datetime, timedelta
import random

from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import SourceTM, SmsTM, Phone, Taxophone, Phone1602

from .taximaster.api import get_current_orders, send_sms
from .utils import check_phone

def index(request):
    return redirect('/admin/')
    
@login_required(login_url='/admin/')
def load(request):
    return render(request, 'load.html')
    
@login_required(login_url='/admin/')
def loading(request):
    phones = str.strip(request.POST.get('phones', '')).replace(',', '').replace('\r', '').replace(' ', '').split('\n')
    for phone in phones:
        tphone = phone
        if len(phone) == 10 and phone[0] != '8':
            tphone = '8' + tphone
        if not check_phone(tphone):
            continue
        try:
            nphone = Phone1602(used=False, phone=tphone, marker='default')
            nphone.save()
        except:
            pass
    return redirect('/admin/')