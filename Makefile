.PHONY: start tests

start:
	@python -m daredevil.api

tests:
	@find . -name '*.pyc' -delete
	@py.test