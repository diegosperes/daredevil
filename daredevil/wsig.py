# -*- coding: utf-8 -*-

import os

from werkzeug.serving import run_simple
from api import app
import settings


path = os.path.realpath(__file__)
path = os.path.dirname(path)

run_simple(settings.daredevil['host'], settings.daredevil['port'],
           app, use_reloader=True,
           ssl_context=('%s/api.crt' % path, '%s/api.key' % path))
