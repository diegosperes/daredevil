.PHONY: start tests app app-stop

start:
	@python -m daredevil.wsig

app:
	@python -m daredevil.api

app-stop:
	@kill `echo \`ps aux | egrep '^.*daredevil\/api\.py'\` | cut -f2 -d ' '`

flake8:
	@flake8 .

tests: flake8
	@find . -name '*.pyc' -delete
	@py.test -m 'not browsertest' --cache-clear || true

	@make app&
	@py.test -m 'browsertest' --cache-clear || true
	@make app-stop
