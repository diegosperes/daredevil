.PHONY: start tests

start:
	@python daredevil/api.py

tests:
	@py.test