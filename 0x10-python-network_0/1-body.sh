#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl "$1" -G -sfL
