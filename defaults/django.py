# -*- coding: utf-8 -*-
# File   @ __init__.py.py
# Create @ 2017/8/10 14:21
# Author @ 819070918@qq.com

from __future__ import absolute_import
from django.conf import settings

from eureka import defaults
from eureka import SimpleEurekaServiceWrapper

if settings:
    try:
        eureka_urls = getattr(settings, 'EUREKA_URLS', defaults.eureka_urls)
        instance = getattr(settings, 'INSTANCE', defaults.instance)
        heartbeat = getattr(settings, 'HEARTBEAT', defaults.heartbeat)
        service_wrapper = SimpleEurekaServiceWrapper(eureka_urls, instance, heartbeat)
        service_wrapper.run()
    except:
        pass

