#!/bin/bash
# Displays size of http response to a request
curl -s -X OPTIONS "$1" | grep Allow | tr -d "Allow: "
