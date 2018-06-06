from django.conf.urls import include, url
from django.contrib import admin
from sms_server_app import views as app_views  

urlpatterns = [
    url(r'^$', app_views.index),
    url(r'^load$', app_views.load),
    url(r'^loading$', app_views.loading),
    url(r'^admin/', include(admin.site.urls)),
]

handler404 = app_views.index
