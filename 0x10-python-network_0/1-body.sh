#!/bin/bash
# Displays size of http response to a request
if [ "$(curl -s -w '%{http_code}\n' -o /dev/null "$1")" -eq 200 ];then curl -s "$1";fi
