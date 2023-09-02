#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and displays\
        the value of the variable X-Request-Id in the response header
        - use the packages `requests` and `sys`
        - value of this variable is different for each request
'''
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url).headers['X-Request-Id']
    print('{}'.format(response))
