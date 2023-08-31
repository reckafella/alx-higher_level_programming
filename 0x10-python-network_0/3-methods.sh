#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl --url "$1" -X OPTIONS -sLiI | sed -n 's/^Allow: //I p'
