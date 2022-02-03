MAKEFLAGS += --silent
.ONESHELL:
.SHELLFLAGS += -exo pipefail -O globstar -O nullglob

.PHONY: all
all: build start

clean:
	trash .venv

build:
	poetry install

start:
	time poetry run python client.py
