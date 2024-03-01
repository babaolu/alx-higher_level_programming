#!/bin/bash
# Displays size of http response to a request
curl -sI "$1" | grep Content-Length | tr -cd "[:digit:]\n"
