# -*- coding: utf-8 -*-

from multiprocessing import Process

from unittest2 import TestCase
from splinter import Browser
from pytest import mark

from daredevil import settings
from daredevil.api import app
from daredevil.modelos.comando import Comando


class FormComandoValidate(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.browser = Browser()

	@classmethod
	def tearDownClass(cls):
		cls.browser.quit()

	def setUp(self):
		Comando.objects().delete()
		self.form = (
			('nome', 'comando123'), 
			('regex', 'comando regex'), 
			('alvo', 'comando alvo'))

	@mark.browsertest
	def test_deve_fazer_fluxo_criacao_comando(self):
		self.assertFalse(Comando.objects())

		self.browser.visit(self._get_url('cms/comando/listagem'))
		self.browser.find_link_by_href('/cms/comando/adicionar').click()

		for field, value in self.form:
			self.browser.fill(field, value)
		self.browser.choose('acao', 'ler')
		self.browser.find_by_css('input[type="submit"]').click()

		self.assertIn('<title>Comando processado com sucesso</title>', self.browser.html)
		self.assertTrue(Comando.objects(slug='comando123'))

	@mark.browsertest
	def test_deve_fazer_fluxo_edicao_comando(self):
		comando = dict(self.form)
		comando['acao'] = 'ler'
		Comando().salvar(comando)

		self.browser.visit(self._get_url('cms/comando/comando123'))
		self.browser.fill('regex', 'comando regex 2')
		self.browser.fill('alvo', 'comando alvo 2')
		self.browser.choose('acao', 'mostrar/esconder')
		self.browser.find_by_css('input[type="submit"]').click()

		self.assertIn('<title>Comando processado com sucesso</title>', self.browser.html)
		self.assertEqual(len(Comando.objects()), 1)

	@mark.browsertest
	def test_deve_fazer_fluxo_delecao_comando(self):
		comando = dict(self.form)
		comando['acao'] = 'ler'
		Comando().salvar(comando)

		self.browser.visit(self._get_url('cms/comando/listagem'))
		self.browser.find_link_by_href('/cms/comando/deletar/comando123').click()

		self.assertFalse(Comando.objects(slug='comando123'))

	def _get_url(self, sufixo):
		return 'http://%s:%s/%s' % (
			settings.daredevil['host'], settings.daredevil['port'], sufixo)
