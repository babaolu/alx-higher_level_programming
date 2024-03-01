#!/bin/bash
# Displays size of http response to a request
curl -sI -X OPTIONS "$1" | grep Allow: | cut -d " " -f2-
