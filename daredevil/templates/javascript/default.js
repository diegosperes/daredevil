{% include 'javascript/annyang.js' %}

var mostrarEsconder = function(seletorCSS){
  $(seletorCSS).toggle();
}

var ler = function(seletorCSS){
  if (window.SpeechSynthesisUtterance !== undefined) {

    var contador = 0;
    var proximaSintese = function(todasSinteseVoz){
      contador++;
      return todasSinteseVoz[contador];
    }

    var todasSinteseVoz = [];
    var container = $(seletorCSS + ' *').text(function(indice, texto){
      var paragrafos = texto.split('.');

      for (i=0; i < paragrafos.length; i++){
        var paragrafo = paragrafos[i];
        if (paragrafo.trim() != ''){
          var sinteseVoz = new SpeechSynthesisUtterance(paragrafo);
          sinteseVoz.lang = 'pt-BR';
          todasSinteseVoz.push(sinteseVoz);
        }
      }

    });

    var totalSinteses = todasSinteseVoz.length - 1;
    for (i=0; i < todasSinteseVoz.length; i++){
      var sinteseVoz = todasSinteseVoz[i]
      if(i == totalSinteses) {
        sinteseVoz.onend = function(){
          annyang.start();
        }
      } else {
        sinteseVoz.onend = function(){
          speechSynthesis.speak(proximaSintese(todasSinteseVoz));
        }
      }
    }

    annyang.abort();
    speechSynthesis.speak(todasSinteseVoz[0]);
  }
}

var initialize = function(){
  var commands = {
    {% for comando in comandos %}
      '{{ comando.regex }}': {{ processa_calback_comando(comando) }},
    {% endfor %}
  }

  if (annyang){
    annyang.addCommands(commands);
    annyang.setLanguage('pt-BR');
    annyang.start();
  }
}

document.onreadystatechange = function () {
  if (document.readyState == "complete") { initialize(); }
}
