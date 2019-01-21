# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:54:21 2019

@author: chenjing
"""

from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.about, name='about'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)