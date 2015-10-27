var initialize = function(){
	var commands = {
		{% for comando in comandos %}
			'{{ comando.regex }}': {{ processa_calback_comando(comando) }},
		{% endfor %}
	}

	annyang.addCommands(commands);
	annyang.start();
}

document.onreadystatechange = function () {
  if (document.readyState == "complete") { initialize(); }
}