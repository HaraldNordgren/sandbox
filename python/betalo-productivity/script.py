#!/usr/bin/env python3

import pprint
import requests
import sys

from ratios import Ratio


TOKEN = sys.argv[1]
HEADERS = {'Authorization': 'token {}'.format(TOKEN)}

start_date = "2017-05-16"

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
        "user:betalo-sweden",
        "is:pr",
        "is:merged",
        "created:>" + start_date,
        "author:" + username,
    ])
    resp = requests.get(u, headers=HEADERS)
    if resp.status_code != 200:
        print(resp)
        sys.exit(1)

    json_resp = resp.json()
    counter[username] = json_resp["total_count"]

result = Ratio.calculate_ratios(counter)
print()
print("Merged Betalo pull requests since {0}:".format(start_date))
pprint.pprint(result)

