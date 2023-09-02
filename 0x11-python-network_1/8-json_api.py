#!/usr/bin/python3
'''
Python script that takes in a letter and sends a POST request to\
        http://0.0.0.0:5000/search_user with the letter as a parameter.

    - The letter must be sent in the variable q
    - If no argument is given, set q=""
    - If the response body is properly JSON formatted and not empty, display\
            the id and name like this: [<id>] <name>

    - Otherwise:
        - Display Not a valid JSON if the JSON is invalid
        - Display No result if the JSON is empty
    - use the package requests and sys
'''
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    if sys.argv[2]:
        q = sys.argv[2]
    else:
        q = ""
    
