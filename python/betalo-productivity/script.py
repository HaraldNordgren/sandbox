#!/usr/bin/env python3

import sys
import pprint
import requests

TOKEN = sys.argv[1]
HEADERS = {'Authorization': 'token {}'.format(TOKEN)}

start_date = "2017-05-16"

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
        u = 'https://api.github.com/search/issues?q=' + "+".join([
            "author:" + username,
            "user:betalo-sweden",
            "is:pr",
            "is:merged",
            "created:>" + start_date,
        ])
        resp = s.get(u)
        if resp.status_code != 200:
            sys.exit(1)

        json_resp = resp.json()
        counter[username] = json_resp["total_count"]

    total_prs = sum(counter.values())
    ratios = {username: prs/total_prs for username, prs in counter.items()}
    sorted_ratios = sorted(ratios.items(), reverse=True, key=lambda kv: kv[1])
    
    result = []
    for ratio_tuple in sorted_ratios:
        username, ratio = ratio_tuple
        result.append((username, "{0:.0%}".format(ratio)))

    print()
    print("Merged Betalo pull requests since {0}:".format(start_date))
    pprint.pprint(result)

