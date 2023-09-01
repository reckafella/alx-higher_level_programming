#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and displays\
        the body of the response (decoded in utf-8).

Manage urllib.error.HTTPError exceptions and print: Error code: followed by\
        the HTTP status code
        - uses `urllib` and `sys` packages
'''
import urllib.request as urlreq
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urlreq.urlopen(url) as response:
            result = response.read().decode('utf-8')
            print('{}'.format(result))
    except urlib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
