# -*- coding: utf-8 -*-

import json

from flask import Flask, render_template, request
from mongoengine import connect

from daredevil.modelos.comando import Comando
import settings

connect(settings.MONGOHOST, settings.MONGOPORT)
app = Flask(__name__)


@app.route('/cms/comando/<rota>', methods=['GET', 'POST'])
def cms_comandos(rota):
	contexto = {}
	contexto['titulo'] = 'Editar comando de voz'
	contexto['comando'] = Comando.objects(slug=rota)[0]
	contexto['acoes'] = Comando.acoes
	url = 'cms/comandos/default.html'

	return render_template(url, **contexto)


@app.route('/cms/comando/listagem', methods=['GET'])
@app.route('/cms/comando', methods=['GET'])
def cms_listagem():
	contexto = {}
	contexto['comandos'] = Comando.objects()

	return render_template('cms/comandos/listagem.html', **contexto)


@app.route('/cms/comando/adicionar', methods=['GET'])
def cms_adicionar_get():
	contexto = {}
	contexto['titulo'] = 'Adicionar comando de voz'
	contexto['comando'] =  {}
	contexto['acoes'] = Comando.acoes

	return render_template('cms/comandos/default.html', **contexto)


@app.route('/cms/comando/adicionar', methods=['POST'])
def cms_adicionar_post():
	contexto = {}
	try:
		Comando().salvar(request.form.to_dict())
		url = 'cms/comandos/sucesso.html'

	except Exception, e:
		contexto['mensagem'] = e.message
		url = 'cms/comandos/error.html'

	return render_template(url, **contexto)

if __name__ == '__main__':
	app.run()
