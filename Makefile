PYTHON := python3
PIP := pip3

default:
	@cat Makefile | grep ^.*: | grep -v :=

test:
	$(PYTHON) -m unittest discover -s tests

install:
	$(PIP) install .

installe:
	$(PIP) install -e .

clean:
	find . | grep __pycache__ | xargs rm -rf
	rm -rf zzz.egg-info/ venv/ docs/

commit: test
	git status
	sleep 5
	git add .
	git commit -am "update"

pub:
	make commit
	git push

black:
	$(PYTHON) -m venv venv
	. venv/bin/activate && $(PIP) install -r requirements.txt
	. venv/bin/activate && black zzz tests/test*

sphinx:
	$(PYTHON) -m venv venv
	. venv/bin/activate && $(PIP) install -r requirements.txt
	mkdir -p docs
	. venv/bin/activate && sphinx-apidoc -fF -o ./docs ./zzz
	make docs

docs:
	cp -v fordocs/* docs
	. venv/bin/activate && cd docs && make html

.PHONY: docs
