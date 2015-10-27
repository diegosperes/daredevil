# -*- coding: utf-8 -*-

from unittest2 import TestCase

from daredevil.api import app as api
from daredevil.modelos.comando import Comando


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

	def test_deve_mostrar_error_para_rota_cms_com_post_comando_adicionar(self):
		comando_acao_invalida = dict(self.comando)
		comando_acao_invalida['acao'] = 'acao'

		comando_sem_acao = dict(self.comando)
		del comando_sem_acao['acao']

		erros = [
			('<h2>Essa ação não é válida, por favor escolha outra ação.</h2>', comando_acao_invalida),
			('<h2>Por favor escolha uma ação.</h2>', comando_sem_acao)
		]

		for mensagem, comando in erros:
			response = self.app.post('/cms/comando/adicionar', data=comando)
			self.assertIn(mensagem, response.data)

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

	def test_deve_deletar_comando_para_rota_cms_comando_deletar(self):
		Comando().salvar(self.comando)
		self.app.get('/cms/comando/deletar/comando123')
		self.assertFalse(Comando.objects())

