# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

VENV ?= venv
PYTHON ?= $(VENV)/bin/python3
PYTHON_VERSION ?= 3.11
FOCAL ?= 2fa-directory
IMAGE ?= lens-focal-$(FOCAL)
DOCKER ?= docker

.PHONY: all
all: focal

.PHONY: setup
setup: $(VENV)/requirements.txt

requirements.txt: requirements.in | $(VENV)
	uv pip compile --python-version $(PYTHON_VERSION) --upgrade -o requirements.txt requirements.in

$(VENV)/requirements.txt: requirements.txt | $(VENV)
	VIRTUAL_ENV=$(VENV) uv pip install -r requirements.txt
	cp -f requirements.txt $(VENV)/requirements.txt

$(VENV):
	uv venv $(VENV)

.PHONY: clean
clean:
	find -name __pycache__ -type d -exec rm -rf '{}' \;
	find -name \*.pyc -type f -exec rm -f '{}' \;

.PHONY: distclean
distclean:
	rm -rf node_modules/ $(VENV)

.PHONY: docker-build
docker-build:
	$(DOCKER) build -t $(IMAGE) .

.PHONY: docker-run
docker-run:
	$(DOCKER) run --rm -it $(IMAGE)

.PHONY: docker-run-bash
docker-run-bash:
	$(DOCKER) run --rm -it $(IMAGE) bash

.PHONY: focal
focal:
	while ! nc -z localhost 6379; do sleep 1 ; done
	celery -A main worker --hostname $(FOCAL)@%h -l INFO -Q $(FOCAL)
