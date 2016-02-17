# -*- coding: utf-8 -*-
from django.conf.urls import url
import service.views


urlpatterns = [
    url(r'^$', service.views.home, name='home'),
    # url(r'^chat/$', service.views.chat, name='chat'),
    url(r'^test/(?P<test_id>\d+)/$', service.views.do_test, name='do_test'),
    url(r'^question/(?P<question_id>\d+)/$', service.views.do_test, name='question'),
]