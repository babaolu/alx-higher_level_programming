#!/bin/bash
# Displays size of http response to a request
if [ "$(curl -sI "$1" | cut -f 2 -d " " | head -n 1)" -eq 200 ]; then curl -s "$1"; fi
