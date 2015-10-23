# -*- coding: utf-8 -*-

from unittest2 import TestCase

from daredevil.api import app as api
from daredevil.modelos.comando import Comando


class FormComandoValidate(TestCase):

	def setUp(self):
		pass

	def test_deve_salvar_comando(self):
		dados = {"nome":"comando123", "regex": "regex", "alvo": "alvo", "acao": "ler"}
		Comando.objects(slug='comando123').delete()
		Comando().salvar(dados)
		self.assertTrue(Comando.objects(slug='comando123'))

	def test_nao_deve_salvar_comando_quando_acao_invalida(self):
		dados = {"nome":"comando123", "regex": "regex", "alvo": "alvo", "acao": "acao"}
		Comando.objects(slug='comando123').delete()

		with self.assertRaises(Exception):
			Comando().salvar(dados)

	def test_nao_deve_salvar_comando_quando_acao_nao_existir(self):
		dados = {"nome":"", "regex": "", "alvo": ""}
		Comando.objects(slug='comando123').delete()

		with self.assertRaises(Exception):
			Comando().salvar(dados)