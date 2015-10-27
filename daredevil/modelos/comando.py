# -*- coding: utf-8 -*-

from mongoengine import Document, StringField, ReferenceField


class Comando(Document):

	acoes = [
		('Callback:', 'callback'),
		('Ler conteudo:', 'ler'),
		('Mostrar e esconder elemento:', 'mostrar/esconder')
	]

	nome = StringField(required=True)
	regex = StringField(required=True)
	alvo = StringField(required=True)
	acao = StringField(required=True)
	slug = StringField(required=True, primary_key=True)

	def salvar(self, dado):

		if 'acao' not in dado:
			raise Exception(u'Por favor escolha uma ação.')

		elif not [acao for texto, acao in self.acoes if dado['acao'] == acao]:
			raise Exception(u'Essa ação não é válida, por favor escolha outra ação.')

		self.slug = dado['nome']
		for atributo, valor in dado.items():
			setattr(self, atributo, valor)

		self.save()

	def excluir(self, slug):
		Comando(slug=slug).delete()