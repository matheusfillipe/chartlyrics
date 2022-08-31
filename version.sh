#!/usr/bin/env bash

# Fix version of pyproject.toml from latest git tag

version_tag=$(git describe --tags --abbrev=0)
version=${version_tag#v}
sed -i "s/^version = .*/version = \"$version\"/" pyproject.toml

