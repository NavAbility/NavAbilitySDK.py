.PHONY: help install test lint linting clean locales update-requirements

PYTHON_VERSION?=python3
VIRTUAL_ENV_DIR?=venv_test

install: $(VIRTUAL_ENV_DIR)
$(VIRTUAL_ENV_DIR):
	$(PYTHON_VERSION) -m venv $(VIRTUAL_ENV_DIR)
	$(VIRTUAL_ENV_DIR)/bin/python setup.py install

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

