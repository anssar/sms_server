from django.db import models

class SourceTM(models.Model):
    name = models.CharField(max_length=128)
    port = models.IntegerField()
    address = models.CharField(max_length=128)
    api_key = models.CharField(max_length=128, blank=True, null=True)
    phone_ways = models.CharField(max_length=128, blank=True, null=True)
    taxophone_ways = models.CharField(max_length=128, blank=True, null=True)
    forbidden_groups = models.CharField(max_length=128, blank=True, null=True)
    marker = models.CharField(max_length=128)

    def __str__(self):
        return '{}'.format(self.name)
        
class SmsTM(models.Model):
    name = models.CharField(max_length=128)
    port = models.IntegerField()
    address = models.CharField(max_length=128)
    api_key = models.CharField(max_length=128)
    sms_text = models.CharField(max_length=256)
    default_send_period = models.IntegerField()
    phone_prefix = models.CharField(max_length=128, blank=True, null=True)
    active = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.name)
        
class SmsSmpp(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    sender = models.CharField(max_length=128)
    active = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.name)
        
class Phone(models.Model):
    phone = models.CharField(max_length=128, unique=True)
    used = models.BooleanField()
    smpp_used = models.BooleanField()
    send_after_seconds = models.IntegerField()
    date = models.DateTimeField()
    marker = models.CharField(max_length=128)

    def __str__(self):
        return '{}'.format(self.phone)
        
class Taxophone(models.Model):
    phone = models.CharField(max_length=128, unique=True)
    used = models.BooleanField()
    smpp_used = models.BooleanField()
    send_after_seconds = models.IntegerField()
    date = models.DateTimeField()
    marker = models.CharField(max_length=128)

    def __str__(self):
        return '{}'.format(self.phone)
        
class Phone1602(models.Model):
    phone = models.CharField(max_length=128, unique=True)
    used = models.BooleanField()
    smpp_used = models.BooleanField()
    marker = models.CharField(max_length=128)

    def __str__(self):
        return '{}'.format(self.phone)
