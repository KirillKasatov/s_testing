# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views
import service.views

urlpatterns = [
    url(r'^service/', include('service.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', django.contrib.auth.views.login, name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, name='logout'),
    url(r'^registration/$', service.views.registration, name='registration'),

    # url(r'^$', 'core.views.home', name='home'),
]
