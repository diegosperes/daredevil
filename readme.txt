## Plataforma de comando de voz

1 - Coloque no hosts o seguinte endereço apontando para o ambiente local:
    -> /etc/hosts:
        127.0.0.1       daredevil.local

# http://www.vivaolinux.com.br/dica/Crie-um-certificado-para-uso-em-SSL
2 - Gere a secrete key e o certificado para a aplicação utilizar o https, ex:
    - openssl genrsa -out api.key 1024
    - openssl req -new -key api.key -x509 -out api.crt -days 999

    obs: Não esqueça de utilizar a mesma url que foi setada na primeira etapa.

3 - Adicione o certificado gerado como "sempre confiavel".

4 - Instale as dependencias utilizando o seguinte comando:
    - pip install -r test-requirements.txt

5 - Utilize o comando do makefile para iniciar a aplicação:
    - make start

obs: Para rodar os teste basta utilizar o seguinte comando do makefile:
    - make tests
