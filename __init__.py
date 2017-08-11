# -*- coding: utf-8 -*-
# File   @ __init__.py.py
# Create @ 2017/8/10 14:21
# Author @ 819070918@qq.com

from __future__ import absolute_import

from .wrappers import SimpleEurekaClientWrapper
from .wrappers import SimpleEurekaServiceWrapper


try:
    from django.conf import settings
    settings.configure()
except ImportError:
    settings = None

if settings:
    try:
        eureka_urls = getattr(settings, 'EUREKA_URLS')
        instance = getattr(settings, 'INSTANCE')
        heartbeat = getattr(settings, 'HEARTBEAT')
        service_wrapper = SimpleEurekaServiceWrapper(eureka_urls, instance, heartbeat)
        service_wrapper.run()
    except:
        pass


VERSION = (1, 0, 1)
__version__ = '.'.join(map(str, VERSION))
__all__ = ['SimpleEurekaClientWrapper', 'SimpleEurekaServiceWrapper']
