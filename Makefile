# Define variables
BRANCH = main
REMOTE = origin
VENV_DIR = .venv
REQ_FILE = requirements.txt

# Default target
all: venv install-requirements pull push

# Pull the latest changes from the remote repository
pull:
	@git pull $(REMOTE) $(BRANCH) --rebase || (echo "Resolve conflicts, then run 'make continue' to finish rebase." && exit 1)

# Continue rebase after resolving conflicts
continue:
	@git rebase --continue || (echo "Resolve conflicts, then run 'make continue' to finish rebase." && exit 1)

# Add and commit resolved files
commit:
	@git add -A
	@git commit -m "Resolved conflicts and integrated remote changes"

# Push changes to the remote repository
push:
	@git push $(REMOTE) $(BRANCH)

# Convenience target for pulling and pushing
sync: pull push

# Create and activate virtual environment
venv:
	@if [ ! -d $(VENV_DIR) ]; then python -m venv $(VENV_DIR); fi
	@echo "Virtual environment setup complete. To activate, run 'source $(VENV_DIR)/bin/activate'."

# Install requirements from requirements.txt
install-requirements: venv
	@source $(VENV_DIR)/bin/activate && pip install -r $(REQ_FILE)

# Freeze current pip environment to requirements.txt
freeze-requirements: venv
	@source $(VENV_DIR)/bin/activate && pip freeze > $(REQ_FILE)
	@echo "Requirements have been frozen to $(REQ_FILE)"

# Help target to display available commands
help:
	@echo "Makefile targets:"
	@echo "  make pull               - Pull changes from the remote repository with rebase"
	@echo "  make continue           - Continue rebase after resolving conflicts"
	@echo "  make commit             - Commit resolved files"
	@echo "  make push               - Push changes to the remote repository"
	@echo "  make sync               - Pull changes and then push local changes"
	@echo "  make venv               - Create and activate a virtual environment"
	@echo "  make install-requirements - Install pip requirements from requirements.txt"
	@echo "  make freeze-requirements  - Freeze current environment to requirements.txt"
	@echo "  make help               - Show this help message"

# To ensure the virtual environment is used within the Makefile
.PHONY: venv install-requirements freeze-requirements pull continue commit push sync help
