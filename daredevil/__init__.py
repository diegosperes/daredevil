# -*- coding: utf-8 -*-

from mongoengine import connect

from daredevil import settings

connect(host=settings.mongodb['host'], port=settings.mongodb['port'])