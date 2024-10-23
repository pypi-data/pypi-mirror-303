PYTHON := python3
PIP := $(PYTHON) -m pip
BUILD := $(PYTHON) -m build
TWINE := $(PYTHON) -m twine

BUILD_DIR = dist
SRC_DIR = src/cimulate
SRC := $(wildcard $(SRC_DIR)/*)
DOCS_DIR = docs

.PHONY: install
install:
	$(PIP) install .

.PHONY: build
build: $(BUILD_DIR)

$(BUILD_DIR): $(SRC)
	$(BUILD) -s

.PHONY: publish
publish: $(BUILD_DIR)
	$(TWINE) upload $(BUILD_DIR)/*

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
	rm -rf **/*.egg-info
	rm -rf $(DOCS_DIR)

.PHONY: docs
docs:
	pdoc -o $(DOCS_DIR) cimulate --docformat google --math
