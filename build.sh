#!/bin/bash
CXX=g++-7 ./build_champsim.sh "$1" "${2:-lru}" "${3:-$1}" > /dev/null 2>&1 || exit 1
ls bin/*-1core-"${3:-$1}"
