#!/bin/bash
# Displays size of http response to a request
curl -s -w '%{http_code}\n' -o /dev/null "$1"
