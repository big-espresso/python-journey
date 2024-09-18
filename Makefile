# define the name of the virtual environment directory
VENV := /Users/jwar/dev/python-journey/venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	$(VENV)/bin/python3 app.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean


# # Define variables
# VENV_DIR := /Users/jwar/dev/python-journey/venv
# PYTHON := $(VENV_DIR)/bin/python
# PIP := $(VENV_DIR)/bin/pip
# ACTIVATE := source $(VENV_DIR)/bin/activate
# SRC_DIR ?= src
# MAIN_PY ?= main.py

# # Include environment variables from .env file if it exists
# -include .env

# # Phony targets are not real files
# .PHONY: help all install init clean test lint run

# # Default target
# all: install lint test

# # Help
# help:
# 	@echo "Usage: make [target] [SRC_DIR=directory]"
# 	@echo ""
# 	@echo "Targets:"
# 	@echo "  help       Display this help guide"
# 	@echo "  all        Setup virtual environment, install dependencies, lint, and run tests"
# 	@echo "  install    Create virtual environment and Install dependencies"
# 	@echo "  init       Activate virtual environment"
# 	@echo "  clean      Remove virtual environment and Python cache files"
# 	@echo "  test       Run tests"
# 	@echo "  lint       Lint the code"
# 	@echo "  run        Run the main application"
# 	@echo ""
# 	@echo "Variables:"
# 	@echo "  SRC_DIR    Directory containing the main.py file (default: src)"
# 	@echo "  MAIN_PY    Main Python script (default: main.py)"

# # Create virtual environment if it doesn't exist and install dependencies
# install:
# 	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
# 	@ $(PIP) install -r requirements.txt


# # Clean up virtual environment and Python cache files
# clean:
# 	rm -rf $(VENV_DIR)
# 	find . -type d -name "__pycache__" -exec rm -r {} +

# # Run tests
# test:
# 	$(ACTIVATE) && pytest tests/

# # Lint the code
# lint:
# 	$(ACTIVATE) && flake8 $(SRC_DIR)/

# # Run the application 
# # Can run with different path like this: make run SRC_DIR=src/day-2 MAIN_PY=script.py
# run:
# 	$(ACTIVATE) && $(PYTHON) $(SRC_DIR)/$(MAIN_PY)

# # Note that make will run each command in a different shell. For this reason we can't create a target for this.
# # This is the reason why we user the && for command chainning
# # The best solution is to simply create an alias:
# # echo "alias activate_venv='source ./venv/bin/activate'" >> ~/.zshrc
# # source ~/.zshrc