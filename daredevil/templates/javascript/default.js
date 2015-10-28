{% include 'javascript/annyang.js' %}

var mostrarEsconder = function(seletorCSS){
	$(seletorCSS).toggle();
}

var ler = function(seletorCSS){
	var elemento = $(seletorCSS);
	var mensagem = '';

	if (elemento.is(':visible'){
		mensagem = $(seletorCSS).text();
	})

	if (window.SpeechSynthesisUtterance !== undefined) {

		var sinteseVoz = new SpeechSynthesisUtterance();
		var voz = window.speechSynthesis.getVoices();
		sinteseVoz.voice = voz[10];
		sinteseVoz.voiceURI = 'native';
		sinteseVoz.volume = 1;
		sinteseVoz.rate = 1;
		sinteseVoz.pitch = 2;
		sinteseVoz.text = mensagem;
		sinteseVoz.lang = 'pt-BR';

		speechSynthesis.speak(sinteseVoz);
	}
}

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
