# -*- coding: utf-8 -*-

from unittest2 import TestCase
from splinter import Browser

from daredevil.api import app as api
from daredevil.modelos.comando import Comando


class FormComandoValidate(TestCase):

	# http://splinter.readthedocs.org/en/latest/drivers/flask.html#
	@classmethod
	def setUpClass(cls):
		api.config['TESTING'] = True
		api.config['DEBUG'] = True
		cls.app = api.test_client()
		cls.browser = Browser()

	@classmethod
	def tearDownClass(cls):
		cls.browser.quit()

	def test_deve_fazer_fluxo_criacao_comando(self):
		pass

	def test_deve_fazer_fluxo_edicao_comando(self):
		pass

	def _get_url(self, sufixo):
		return '%s/%s' % (api.config['SERVER_NAME'], sufixo)