MAKEFLAGS += --silent
.ONESHELL:
.SHELLFLAGS += -exo pipefail -O globstar -O nullglob

.PHONY: all
all: js ts python

clean:
	trash generated node_modules .venv

js:
	pnpm install
	mkdir -p generated/js/
	grpc_tools_node_protoc \
		--js_out=import_style=commonjs,binary:./generated/js/ \
		--grpc_out=grpc_js:./generated/js/ \
		--proto_path=../../ \
		helloworld.proto

ts:
	pnpm install
	mkdir -p generated/ts/
	grpc_tools_node_protoc \
		--js_out=import_style=commonjs,binary:./generated/ts/ \
		--grpc_out=grpc_js:./generated/ts/ \
		--plugin=protoc-gen-grpc=./node_modules/.bin/grpc_tools_node_protoc_plugin \
		--proto_path=../../ \
		helloworld.proto

	grpc_tools_node_protoc \
		--plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts \
		--ts_out=./generated/ts/ \
		--proto_path=../../ \
		helloworld.proto

python:
	poetry install
	mkdir -p generated/python/
	poetry run python -m grpc_tools.protoc \
		--python_out=./generated/python/ \
		--grpc_python_out=./generated/python/ \
		--proto_path=../../ \
		helloworld.proto
