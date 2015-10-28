.PHONY: web-start web-stop tests app app-stop flake8 app-test-start app-test-stop start stop

stop:
	@make web-stop&
	@make app-test-stop&

start:
	@make web-start&
	@make app-test-start&

web-start:
	@python -m daredevil.wsig

web-stop:
	@kill `echo \`ps aux | egrep '^.*daredevil\/wsig\.py'\` | cut -f2 -d ' '`

app:
	@python -m daredevil.api

app-stop:
	@kill `echo \`ps aux | egrep '^.*daredevil\/api\.py'\` | cut -f2 -d ' '`

app-test-start:
	@python app-test/wsig.py

app-test-stop:
	@kill `echo \`ps aux | egrep '^.*app-test\/wsig\.py'\` | cut -f2 -d ' '`

flake8:
	@flake8 .

tests: flake8
	@find . -name '*.pyc' -delete
	@py.test -m 'not browsertest' --cache-clear || true

	@make app&
	@py.test -m 'browsertest' --cache-clear || true
	@make app-stop
