# -*- coding: utf-8 -*-

from unittest2 import TestCase
from mongoengine import connect

from daredevil.api import app as api
from daredevil.modelos.comando import Comando


connect(host='127.0.0.1', port=27017)


class TestApi(TestCase):

	comando = dict(nome='comando123', regex='regex-teste', alvo='alvo-teste', acao='ler')

	def setUp(self):
		api.config['TESTING'] = True
		api.config['DEBUG'] = True
		self.app = api.test_client()
		Comando.objects(slug='comando123').delete()

	def test_deve_retornar_pagina_correta_para_rota_cms_comando(self):
		urls = ('/cms/comando', '/cms/comando/listagem')

		for url in urls:
			response = self.app.get(url)
			self.assertEqual(200, response.status_code)
			self.assertEqual('text/html', response.mimetype)
			self.assertIn('<title>Listagem de comandos de voz</title>', response.data)

	def test_deve_retornar_comandos_para_rota_cms_comando_listagem(self):
		comando = dict(self.comando)
		comando['nome'] = 'comando456'

		Comando().salvar(self.comando)
		Comando().salvar(comando)

		response = self.app.get('/cms/comando/listagem')
		self.assertIn('<a href="/cms/comando/comando123">comando123</a>', response.data)
		self.assertIn('<a href="/cms/comando/comando456">comando456</a>', response.data)

	def test_deve_retornar_pagina_correta_para_rota_cms_comando_adicionar(self):
		response = self.app.get('/cms/comando/adicionar')
		self.assertEqual(200, response.status_code)
		self.assertEqual('text/html', response.mimetype)
		self.assertIn('<title>Adicionar comando de voz</title>', response.data)

	def test_deve_retornar_pagina_sucesso_para_rota_cms_com_post_comando_adicionar(self):
		response = self.app.post('/cms/comando/adicionar', data=self.comando)
		self.assertEqual(200, response.status_code)
		self.assertEqual('text/html', response.mimetype)
		self.assertIn('<title>Comando processado com sucesso</title>', response.data)

	def test_deve_retornar_pagina_error_para_rota_cms_com_post_comando_adicionar(self):
		response = self.app.post('/cms/comando/adicionar', data=dict(
			nome='comando123', regex='regex', alvo='alvo', acao='acao'))
		self.assertEqual(200, response.status_code)
		self.assertEqual('text/html', response.mimetype)
		self.assertIn('<title>Error ao processar comando</title>', response.data)

	def test_deve_mostrar_error_acao_para_rota_cms_com_post_comando_adicionar(self):
		response = self.app.post('/cms/comando/adicionar', data=dict(
			nome='comando123', regex='regex', alvo='alvo', acao='acao'))
		self.assertIn('<h2>Essa ação não é válida, por favor escolha outra ação.</h2>', response.data)

	def test_deve_retornar_pagina_correta_para_rota_edicao_cms_comando(self):
		Comando().salvar(self.comando)
		response = self.app.get('/cms/comando/comando123')
		self.assertEqual(200, response.status_code)
		self.assertEqual('text/html', response.mimetype)
		self.assertIn('<title>Editar comando de voz</title>', response.data)

	def test_deve_retornar_pagina_com_informacoes_para_rota_edicao_cms_comando(self):
		Comando().salvar(self.comando)
		response = self.app.get('/cms/comando/comando123')
		self.assertIn('comando123', response.data)
		self.assertIn('regex-teste', response.data)
		self.assertIn('alvo-teste', response.data)
		self.assertIn('checked="checked"', response.data) # ação: ler

	def test_deve_salvar_comando_para_rota_cms_comando_adicionar(self):
		self.app.post('/cms/comando/adicionar', data=self.comando)
		self.assertTrue(Comando.objects(slug='comando123'))
