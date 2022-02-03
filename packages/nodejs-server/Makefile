MAKEFLAGS += --silent
.ONESHELL:
.SHELLFLAGS += -exo pipefail -O globstar -O nullglob

.PHONY: all
all: build start

clean:
	trash node_modules

build:
	pnpm install

start:
	node server.js