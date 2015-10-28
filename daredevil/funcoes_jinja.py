

def processa_calback_comando(comando):
    callback = None

    if comando.acao == 'ler':
        callback = 'ler("%s");' % comando.alvo

    elif comando.acao == 'mostrar/esconder':
        callback = 'mostrarEsconder("%s");' % comando.alvo

    else:
        callback = comando.alvo

    return 'function(){%s}' % callback
