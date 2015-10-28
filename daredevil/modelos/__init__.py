# -*- coding: utf-8 -*-

from mongoengine import connect

try:
    from daredevil import settings
except:
    import settings

connect(host=settings.mongodb['host'], port=settings.mongodb['port'])
