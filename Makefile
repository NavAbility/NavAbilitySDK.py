.PHONY: help install test docs release lint clean

PYTHON_VERSION?=python3
VIRTUAL_ENV_DIR?=venv_test
SDKPY_DOCS_BUILDER?=jupyter-book

install: $(VIRTUAL_ENV_DIR)
$(VIRTUAL_ENV_DIR):
	$(PYTHON_VERSION) -m venv $(VIRTUAL_ENV_DIR)
	$(VIRTUAL_ENV_DIR)/bin/$(PYTHON_VERSION) setup.py install

release: $(VIRTUAL_ENV_DIR)
	rm -rf dist
	$(VIRTUAL_ENV_DIR)/bin/$(PYTHON_VERSION) setup.py sdist
	# Assuming you have twine already in the sdist
	$(VIRTUAL_ENV_DIR)/bin/pip install twine
	$(VIRTUAL_ENV_DIR)/bin/twine upload dist/*.tar.gz

docs_cicd:
	$(PYTHON_VERSION) -m venv venv_docs
	. venv_docs/bin/activate
	pip install --upgrade pip
	pip install -r docs/requirements.txt
	pip install .
	$(SDKPY_DOCS_BUILDER) build docs/

docs: 
	$(SDKPY_DOCS_BUILDER) build docs/
	$(SDKPY_DOCS_BUILDER) build docs/

docs_firefox: docs
	firefox docs/_build/html/index.html

# typically, phony make targets are imperatives.
lint: install
	tox -e lint

test: install
	tox

clean:
	rm -rf $(TESTING_CONFIG_DIR)
	rm -rf build *.egg-info
	find -name "*.pyc" -delete
	find -name "__pycache__" -delete
	rm -rf $(VIRTUAL_ENV_DIR)
	rm -rf tar-source
	rm -f *.tar.gz

