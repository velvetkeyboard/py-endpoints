project=endpoints
venv=env
python=$(venv)/bin/python
linter=$(venv)/bin/flake8
pypi_mode=test

project_version=$(shell $(python) -c "from $(project) import __version__; print(__version__)")
git_version=$(shell git describe --tags)

ifeq ($(pypi_mode),test)
	pypi_url=https://test.pypi.org/legacy/
endif
ifeq ($(pypi_mode),production)
	pypi_url=https://upload.pypi.org/legacy/
endif


test:
	$(python) -m unittest

lint:
	$(linter) endpoints/
	$(linter) tests.py

build_pypi: lint
	$(python) setup.py bdist_wheel

check_semver:
ifneq ($(git_version),$(project_version))
	@echo "[$(git_version)] != [$(project_version)]"
	exit 1
endif

publish_pypi: lint check_semver build_pypi
	twine upload \
		--repository-url $(pypi_url) \
		dist/$(project)-$(project_version)-py3-none-any.whl
