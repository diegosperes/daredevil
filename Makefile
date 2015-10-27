.PHONY: start tests stop

start:
	@python -m daredevil.api


stop:
	@kill `echo \`ps aux | egrep '^.*daredevil\/api\.py'\` | cut -f2 -d ' '`

tests:
	@find . -name '*.pyc' -delete
	@py.test -m 'not browsertest' --cache-clear || true

	@make start&
	@py.test -m 'browsertest' --cache-clear || true
	@make stop