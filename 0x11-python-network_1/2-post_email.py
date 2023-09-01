#!/usr/bin/python3
'''
Python script that takes in a URL and an email, sends a POST request to the\
        passed URL with the email as a parameter, and displays the body of\
        the response (decoded in utf-8)
        - uses `urllib` and `sys` packages
'''
import urllib.request as urlreq
import urllib.parse as urlparser
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': str(sys.argv[2])}
    data = urlparser.urlencode(values)
    data = data.encode('utf-8')
    request = urlreq.Request(url, data)

    with urlreq.urlopen(request) as response:
        result = response.read().decode('utf-8')
        print('Your email is: {}'.format(result))
