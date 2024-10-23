VENV_NAME=strideutils
CONDA_BASE := $(shell conda info --base)/envs
VENV_BIN=$(CONDA_BASE)/$(VENV_NAME)/bin
PYTHON=$(VENV_BIN)/python

install:
	conda create --name $(VENV_NAME) python=3.11 -y
	$(PYTHON) -m pip install -e .[dev]

lint:
	@echo "Linting..."
	@$(VENV_BIN)/flake8 --max-line-length 120 --exclude .ipynb_checkpoints strideutils

type-check:
	@echo "Type checking..."
	@$(VENV_BIN)/mypy strideutils

format:
	@echo "Formatting..."
	@$(VENV_BIN)/black --skip-string-normalization --line-length 120 strideutils

tidy: lint type-check format

test:
	@echo "Running unit tests..."
	@$(VENV_BIN)/pytest . -v