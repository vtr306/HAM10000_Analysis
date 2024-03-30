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
	@rm -rf ham10000_codes/*.egg-info
	@rm -rf htmlcov
	@rm -rf docs/_build
	@rm -rf docs/_static


.PHONY: install
install:		## Install in development mode.
	pip install -e .[test]


.PHONY: format
format:			## Format code using isort and black
	isort ham10000_codes/
	isort tests/
	black -l 110 ham10000_codes/
	black -l 110 tests/


.PHONY: lint
lint:			## Run linters
	flake8 ham10000_codes/
	black -l 110 --check ham10000_codes/
	black -l 110 --check tests/
	mypy ham10000_codes/


.PHONY: test
test: lint		## Run tests and generate coverage report
	pytest tests/
	coverage html


.PHONY: docs
docs:			## Build documentation
	@echo "Building documentation..."
	pdoc ham10000_codes -o docs
	@echo "Serving API documentation..." 
	pdoc ham10000_codes --host localhost --port 8080
