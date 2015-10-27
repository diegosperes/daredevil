

def processa_calback_comando(comando):
	if comando.acao == 'ler':
		return 'ler("%s");' % comando.alvo

	if comando.acao == 'mostrar/esconder':
		return 'mostrarEsconder("%s");' % comando.alvo

	else:
		return comando.alvo