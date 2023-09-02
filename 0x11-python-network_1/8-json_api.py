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
    url = 'http://0.0.0.0:5000/search_user'
    if sys.argv[1]:
        q = sys.argv[1]
    else:
        q = ""
    try:
        with requests.post(url, data=q) as response:
            result = response.json()
            if result:
                print('[{}] {}'.format(result.get('id'), result.get('name')))
            else:
                print('No result')

    except requests.exceptions.JSONDecodeError as e:
        print('Not a valid JSON')
