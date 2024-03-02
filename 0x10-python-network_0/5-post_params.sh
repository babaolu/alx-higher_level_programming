#!/bin/bash
# Displays size of http response to a request
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
