#!/usr/bin/python3
"""
script to print the x-request-id
"""
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    headers = dict(response.info())
    print(headers.get("X-Request-Id"))
