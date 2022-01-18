.PHONY: help install test release lint clean

PYTHON_VERSION?=python3
VIRTUAL_ENV_DIR?=venv_test

install: $(VIRTUAL_ENV_DIR)
$(VIRTUAL_ENV_DIR):
	$(PYTHON_VERSION) -m venv $(VIRTUAL_ENV_DIR)
	$(VIRTUAL_ENV_DIR)/bin/python setup.py install

release: $(VIRTUAL_ENV_DIR)
	rm -rf dist
	$(PYTHON_VERSION) setup.py sdist
	# Assuming you have twine already in the sdist
	pip install twine
	twine upload dist/*

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

