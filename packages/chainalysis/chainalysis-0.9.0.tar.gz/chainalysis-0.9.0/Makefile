.PHONY: test coverage clean test-coverage

# Run tests
test:
	PYTHONPATH=src python -m unittest discover src/test/

# Run specific test suite
test-suite:
	PYTHONPATH=src python -m unittest src/test/$(TEST_SUITE)/tests.py

# Run specific e2e test suite
test-e2e-suite:
	PYTHONPATH=src python -m unittest src/test/e2e/$(TEST_SUITE).py

# Run a specific e2e test case
test-e2e-case:
	PYTHONPATH=src python -m unittest src.test.e2e.$(TEST_SUITE).$(TEST_CLASS).$(TEST_CASE)

# Run tests with coverage
coverage:
	rm -rf .coverage  # Clean old coverage data
	PYTHONPATH=src coverage run --source=src -m unittest discover src/test/
	coverage report -m --omit="src/test/*"

upload-module:
	rm -rf dist
	python -m build
	twine upload dist/*

# Create documentation
document:
	find ./src/sphinx -type f -name '*.rst' ! -name 'index.rst' -exec rm -f {} + 2>/dev/null
	sphinx-apidoc -o ./src/sphinx ./src/chainalysis
	make -C ./src/sphinx clean
	make -C ./src/sphinx html
	cp -R ./src/sphinx/_build/html/ ./docs/
