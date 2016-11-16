#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^checkcode/', views.checkcode),
]
