.PHONY: help
help:			## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets: "
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: clean
clean:			## Clean unused files.
	@echo "Cleaning up..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -delete
	@rm -f .coverage
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf HAM10000 Analysis/*.egg-info
	@rm -rf htmlcov
	@rm -rf docs/_build
	@rm -rf docs/_static


.PHONY: install
install:		## Install in development mode.
	pip install -e .[test]


.PHONY: format
format:			## Format code using isort and black
	isort HAM10000 Analysis/
	isort tests/
	black -l 110 HAM10000 Analysis/
	black -l 110 tests/


.PHONY: lint
lint:			## Run linters
	flake8 HAM10000 Analysis/
	black -l 110 --check HAM10000 Analysis/
	black -l 110 --check tests/
	mypy HAM10000 Analysis/


.PHONY: test
test: lint		## Run tests and generate coverage report
	pytest tests/
	coverage html


.PHONY: docs
docs:			## Build documentation
	@echo "Building documentation..."
	pdoc HAM10000 Analysis -o docs
	@echo "Serving API documentation..." 
	pdoc HAM10000 Analysis --host localhost --port 8080
