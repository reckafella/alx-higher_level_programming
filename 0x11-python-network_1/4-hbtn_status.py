#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status

    - use the package requests
'''
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    result = requests(url).content.decode('utf-8')
    print('{}'.format(result))
