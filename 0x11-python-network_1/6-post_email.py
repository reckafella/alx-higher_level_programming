#!/usr/bin/python3
'''
Python script that takes in a URL and an email address, sends a POST request\
         to the passed URL with the email as a parameter, and finally\
         displays the body of the response.

    - The email must be sent in the variable email
    - use the packages `requests` and `sys`
'''
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': str(sys.argv[2])}

    with requests.post(url, data=values) as response:
        result = response.content.decode('utf-8')
        print('{}'.format(result))
