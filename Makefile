
SRC_DIR := src
SRC := $(wildcard *.py) $(wildcard src/*/*.py)
TEST_SRC := $(wildcard test/*/test_*?.py)

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

args := $(or ${ARGS}, null)
single_test:
ifeq (${args},null)
# Alternatively, could just do: ifeq (${ARGS},)
	@echo "You need to provide the filter string, e.g. make single_test ARGS=day_1"
else
	@echo "Running Test using pytest with the filter option (-k)"
	@echo "=========================="
	@echo "Testing: ${TEST_SRC} against filter ${ARGS}"
	python -m pytest -s -vv --cov=${SRC_DIR} -k ${ARGS} ${TEST_SRC}
endif

tests:
	@echo "Running Tests using pytest"
	@echo "=========================="
	@echo "Testing: ${TEST_SRC}"
	python -m pytest -s -vv --cov=${SRC_DIR} ${TEST_SRC}

format:
	@echo "Formatting using black"
	@echo "======================"
	black ${SRC}

lint:
	@echo "Running lint"
	@echo "============"
	pylint --disable=R,C --ignore-patterns=${TEST_SRC} ${SRC}

refactor: format lint

all: install lint test format