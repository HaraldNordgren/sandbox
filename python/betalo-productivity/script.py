#!/usr/bin/env python3

import sys
import pprint
import requests

TOKEN = sys.argv[1]
HEADERS = {'Authorization': 'token {}'.format(TOKEN)}

with requests.Session() as s:
    s.headers.update(HEADERS)

    counter = {}

    users = [
        "alesr",
        "ashrafansari",
        "djui",
        "frozendragon498",
        "haraldnordgren",
        "jeespers",
        "rgpfc",
    ]

    for username in users:
        keys = [
            "author:" + username,
            "user:betalo-sweden",
            "is:pr",
            "is:merged",
            "created:>2017-05-16",
        ]
        u = 'https://api.github.com/search/issues?q=' + "+".join(keys)
        
        resp = s.get(u)
        if resp.status_code != 200:
            sys.exit(1)

        result = resp.json()
        #print(result["total_count"])
        #print(result["items"][0]["user"]["login"])

        counter[username] = result["total_count"]

    total = sum(counter.values())
    ratios = {}
    for username, prs in counter.items():
        #ratios[username] = "{0:.0%}".format(prs / total)
        ratios[username] = prs / total

    sorted_ratios = sorted(ratios.items(), reverse=True, key=lambda kv: kv[1])
    result = []
    for v in sorted_ratios:
        k, vv = v
        result.append((k, "{0:.0%}".format(vv)))
    pprint.pprint(result)
