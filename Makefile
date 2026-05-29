VENV_DIR ?= .venv
PYTHON ?= python3
PIP := $(VENV_DIR)/bin/pip

.PHONY: venv syntax-check check encrypt-vault deploy deploy-pass task

venv:
	@if [ ! -x "$(PIP)" ]; then \
		$(PYTHON) -m venv "$(VENV_DIR)"; \
		"$(PIP)" install --upgrade pip; \
		"$(PIP)" install -r requirements.txt; \
	fi
	mkdir -p charts

train: venv
	.venv/bin/python src/train.py

predict: venv
	.venv/bin/python src/predict.py	