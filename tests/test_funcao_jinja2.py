from unittest2 import TestCase
from daredevil.modelos.comando import Comando
from daredevil.funcoes_jinja import processa_calback_comando


class TestFuncaoJinja2(TestCase):

    def test_deve_processar_callback_comando(self):
        comandos = (
            ({"nome": "comando123", "regex": "regex", "alvo": "chamarCallback",
             "acao": "callback"}, 'function(){chamarCallback}'),
            ({"nome": "comando123", "regex": "regex", "alvo": "seletorCSS",
             "acao": "ler"}, 'function(){ler("seletorCSS");}'),
            ({"nome": "comando123", "regex": "regex", "alvo": "seletorCSS",
             "acao": "mostrar/esconder"},
             'function(){mostrarEsconder("seletorCSS");}'))

        for dado, callback in comandos:
            comando = Comando()
            comando.salvar(dado)
            self.assertEqual(callback, processa_calback_comando(comando))
