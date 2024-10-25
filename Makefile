SHELL := bash
CREATE_ZIP ?= "TRUE"
OFFLINE_DOCS ?= "FALSE"
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.DEFAULT: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:  ## build python distributable artifacts.
	python -m build --wheel --sdist
.PHONY: build

clean-build: ## Remove build artifacts.
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
.PHONY: clean-build

clean-pyc: ## Remove python artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
.PHONY: clean-pyc

venv: ## Create a virtual environment.
	python3.9 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
	venv/bin/pip install --upgrade wheel
	venv/bin/pip install pip-tools
.PHONY: venv

dependencies: ## Installs packages in requirements.txt into the virtual environment.
	pip install -r requirements.txt
.PHONY: dependencies

test-dependencies: ## Installs packages in test_requirements.txt into the virtual environment.
	pip install -r test_requirements.txt
.PHONY: test-dependencies

doc-dependencies: ## Installs packages in doc_requirements.txt into the virtual environment.
	pip install -r doc_requirements.txt
.PHONY: doc-dependencies

all-dependencies: dependencies test-dependencies doc-dependencies  ## Installs all packages.
.PHONY: all-dependencies

update-dependencies:  ## Updates all of the dependency files to the latest versions
	pip install pip-tools
	pip-compile requirements.in > requirements.txt
	pip-compile test_requirements.in > test_requirements.txt
	pip-compile doc_requirements.in > doc_requirements.txt
.PHONY: update-dependencies

clean-venv: ## Uninstall all packages in virtual environment.
	pip freeze | xargs pip uninstall -y
.PHONY: clean-venv

build-docs: ## Build the html documentation.
	if [ $(OFFLINE_DOCS) = "FALSE" ]; then \
		echo "Building online documentation."; \
  		unset OFFLINE && export PYTHONPATH=./ && mkdocs build; \
	else \
	  	echo "Building offline documentation."; \
		export OFFLINE="true" && export PYTHONPATH=./ && mkdocs build; \
	fi
.PHONY: build-docs

view-docs: ## Start a web browser pointed at the html documentation.
	open ./site/index.html
.PHONY: view-docs

clean-docs: ## Delete all files in the /docs/build directory.
	rm -rf site
.PHONY: clean-docs

unit-tests: clean-pyc  ## Run all tests found in the /tests directory.
	py.test --verbose --color=yes ./tests/unit
.PHONY: unit-tests

test-reports: clean-pyc clean-test ## Run all tests found in the /tests directory and output unit test and code coverage reports.
	# creating the directory to hold unit test reports, if it doesn't exist
	mkdir -p coverage_reports

	# running the unit test suite with coverage
	python -m pytest --cov=tests --cov-report=html:coverage_reports/html_report --cov-report=xml:coverage_reports/test_coverage.xml --html=coverage_reports/unit_test_report.html --self-contained-html --junitxml=coverage_reports/unit_tests.xml --verbose --color=yes ./tests/unit

	if [ $(CREATE_ZIP) = "TRUE" ]; then \
	zip -r ./coverage_reports/coverage_report.zip ./coverage_reports/html_report && \
	rm -rf ./coverage_reports/html_report; \
	fi

	# deleting the original coverage data file
	rm -rf .coverage
.PHONY: test-reports

clean-test: ## Delete the pytest cache files.
	rm -rf .pytest_cache
	rm -rf coverage_reports
	rm -rf .coverage
.PHONY: clean-test

check-codestyle:  ## Check the style of the code.
	pycodestyle tests
.PHONY: check-codestyle

check-docstyle:  ## Check the style of the docstrings.
	pydocstyle tests --match='.*\.py'
.PHONY: check-docstyle

check-security:  ## Checks for common security vulnerabilities.
	bandit -c bandit.yaml
.PHONY: check-security
