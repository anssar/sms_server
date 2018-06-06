from django.contrib import admin

from .models import SourceTM, SmsTM, Phone, Taxophone, Phone1602, SmsSmpp

class TaxophoneAdmin(admin.ModelAdmin):
    list_filter = ('used',)
    
admin.site.register(Taxophone, TaxophoneAdmin)
admin.site.register(Phone)
admin.site.register(Phone1602)
admin.site.register(SmsTM)
admin.site.register(SmsSmpp)
admin.site.register(SourceTM)
