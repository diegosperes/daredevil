.PHONY: start tests

start:
	@python daredevil/api.py

tests:
	@find . -name '*.pyc' -delete
	@py.test