# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

from modelos.comando import Comando
from funcoes_jinja import processa_calback_comando
import settings

app = Flask(__name__)


@app.context_processor
def funcoes_jinja2():
    return dict(processa_calback_comando=processa_calback_comando)


@app.route('/javascript', methods=['GET'])
def javascript():
    contexto = {}
    contexto['comandos'] = Comando.objects()
    return render_template('javascript/default.js', **contexto)


@app.route('/cms/comando/<slug>', methods=['GET'])
def cms_comandos(slug):
    contexto = {}
    contexto['titulo'] = 'Editar comando de voz'
    contexto['comando'] = Comando.objects(slug=slug)[0]
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
    contexto['comando'] = {}
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


@app.route('/cms/comando/deletar/<slug>', methods=['GET'])
def cms_deletar_get(slug):
    Comando().excluir(slug)

    return render_template('cms/comandos/sucesso.html')

if __name__ == '__main__':
    app.run(host=settings.daredevil['host'], port=settings.daredevil['port'], debug=settings.daredevil['debug'])
