PYTHON := python3
PIP := pip3

default:
	@cat Makefile | grep ^.*: | grep -v ":=" | grep -v "^\." | sort

all: clean black test sphinx

test:
	$(PYTHON) -m unittest discover -s tests

install:
	$(PIP) install .

installe:
	$(PIP) install -e .

clean:
	find . | grep __pycache__ | xargs rm -rf
	rm -rf zzz.egg-info/ venv/ docs/

commit: test clean
	git status
	sleep 5
	git add .
	git commit -am "update"

pub:
	make commit
	git push

requirements:
	$(PYTHON) -m venv venv
	. venv/bin/activate && $(PIP) install -r requirements.txt

black: requirements
	make cformat
cformat:
	. venv/bin/activate && black zzz tests/test*

sphinx: requirements
	mkdir -p docs
	. venv/bin/activate && sphinx-apidoc -fF -o ./docs ./zzz
	make docs
docs:
	cp -v fordocs/* docs
	. venv/bin/activate && cd docs && make html

.PHONY: docs
