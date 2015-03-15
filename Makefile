.PHONY: clean-pyc clean-build clean deps develop docs lint coverage tests

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "develop - install all packages required for development"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "docs - generate Sphinx HTML documentation, including API docs"

clean: clean-build clean-pyc

deps:
	pip install -e .
	pip install "file://`pwd`#egg=pytest-django-casperjs[tox]"
	pip install "file://`pwd`#egg=pytest-django-casperjs[docs]"
	pip install "file://`pwd`#egg=pytest-django-casperjs[tests]"
	pip install "file://`pwd`#egg=pytest-django-casperjs[postgresql]"
	pip install "file://`pwd`#egg=pytest-django-casperjs[mysql]"

docs: clean-build
	sphinx-apidoc --force -o docs/source/modules/ src/pytest_django_casperjs src/pytest_django_casperjs/tests
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

clean-build:
	rm -fr build/ src/build
	rm -fr dist/ src/dist
	rm -fr *.egg-info src/*.egg-info
	rm -fr htmlcov/
	$(MAKE) -C docs clean

lint:
	flake8 pytest-django-casperjs --ignore='E122,E124,E125,E126,E128,E501,F403' --exclude="**/migrations/**"

tests:
	py.test src/

coverage:
	py.test --clearcache --cov {toxinidir}/src/pytest-django-casperjs

test-all:
	tox
