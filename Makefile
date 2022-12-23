
SRC := $(wildcard *.py) $(wildcard funcLog/*.py)
TEST_SRC := $(wildcard test_.*?py)

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main ${TEST_SRC}

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