# -*- coding: utf-8 -*-

import os

from werkzeug.serving import run_simple
from app_test import app


path = os.path.realpath(__file__)
path = os.path.dirname(path)
path = os.path.dirname(path) + '/daredevil'

run_simple('0.0.0.0', 8888,
           app, use_reloader=True,
           ssl_context=('%s/api.crt' % path, '%s/api.key' % path))
