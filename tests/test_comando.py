# -*- coding: utf-8 -*-

from unittest2 import TestCase

from daredevil.modelos.comando import Comando


class FormComandoValidate(TestCase):

	def setUp(self):
		Comando.objects(slug='comando123').delete()

	def test_deve_salvar_comando(self):
		dados = {"nome":"comando123", "regex": "regex", "alvo": "alvo", "acao": "ler"}
		Comando().salvar(dados)
		self.assertTrue(Comando.objects(slug='comando123'))

	def test_nao_deve_salvar_comando_quando_acao_invalida(self):
		dados = {"nome":"comando123", "regex": "regex", "alvo": "alvo", "acao": "acao"}
		with self.assertRaises(Exception):
			Comando().salvar(dados)

	def test_nao_deve_salvar_comando_quando_acao_nao_existir(self):
		dados = {"nome":"", "regex": "", "alvo": ""}
		with self.assertRaises(Exception):
			Comando().salvar(dados)

	def test_deve_excluir_comando(self):
		dados = {"nome":"comando123", "regex": "regex", "alvo": "alvo", "acao": "ler"}
		Comando().salvar(dados)
		Comando().excluir('comando123')
		self.assertFalse(Comando.objects(slug='comando123'))