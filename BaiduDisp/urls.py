#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @author: peidehao

from django.conf.urls import url
from . import views

urlpatterns=[
    url('^info',views.display),
    url('^save',views.save)
]
