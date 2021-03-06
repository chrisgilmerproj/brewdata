#! /usr/bin/make 

PACKAGE_NAME=brewdata

VENV_DIR?=.venv
VENV_ACTIVATE=$(VENV_DIR)/bin/activate
WITH_VENV=. $(VENV_ACTIVATE);

TEST_OUTPUT?=nosetests.xml
COVERAGE_OUTPUT?=coverage.xml

.PHONY: help venv setup clean teardown lint test package upload install scrape_cereals scrape_hops scrape_yeast

help:  ## Print the help documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

$(VENV_ACTIVATE): requirements.txt
	test -f $@ || virtualenv --python=python2.7 $(VENV_DIR)
	$(WITH_VENV) pip install --no-deps -r requirements.txt
	touch $@

venv: $(VENV_ACTIVATE)

setup: venv

clean: ## Clean the library and test files
	python setup.py clean
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg*/
	rm -f MANIFEST
	rm -f $(TEST_OUTPUT)
	coverage erase || rm -f .coverage
	rm -f $(COVERAGE_OUTPUT)
	find ./ -type d -name '__pycache__' -delete
	find ./ -type f -name '*.pyc' -delete

teardown: ## Remove all virtualenv files
	rm -rf $(VENV_DIR)/
	rm -rf .tox/

lint: venv ## Run linting tests
	$(WITH_VENV) flake8 $(PACKAGE_NAME)/

test:  ## Run unit tests
	tox

package: clean ## Create the python package
	python setup.py build sdist check

upload: clean ## Upload the python package
	python setup.py build sdist check upload -r pypi

install:  ## Install the python package
	$(WITH_VENV) python setup.py install

default: help

scrape_cereals: venv ## Scrape cereals data
	$(WITH_VENV) scrapy runspider scraper/spiders/cereals_spider.py

scrape_hops: venv ## Scrape hops data
	$(WITH_VENV) scrapy runspider scraper/spiders/hops_spider.py

scrape_yeast: venv ## Scrape yeast data
	$(WITH_VENV) scrapy runspider scraper/spiders/yeast_spider.py
