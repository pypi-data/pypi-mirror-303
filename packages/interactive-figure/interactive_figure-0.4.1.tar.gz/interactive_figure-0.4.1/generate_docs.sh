#!/usr/bin/env bash

script_src=$(dirname "$0")
sphinx-build -b html "${script_src}/docs_source" "${script_src}/docs"