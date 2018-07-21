#!/usr/bin/env python3

import sys
import requests

TOKEN = sys.argv[1]
HEADERS = {'Authorization': 'token {}'.format(TOKEN)}

with requests.Session() as s:
    s.headers.update(HEADERS)
    #r = s.get('https://api.github.com/user')

    keys = [
        "is:merged",
        "is:pr",
        "author:rgpfc",
        "user:betalo-sweden",
        "created:>2017-05-16",
    ]
    query = "+".join(keys)
    u = 'https://api.github.com/search/issues?q=' + query
    
    r = s.get(u)

    print(r.status_code)
    result = r.json()
    print(result["total_count"])

