#!/usr/bin/env python3

import sys
import pprint
import requests
from requests.auth import HTTPBasicAuth

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

start_date = "2017-05-16"

counter = {}
users = [
    "alessandro.resta",
    "ashraf.ansari",
    "uwe.dauernheim",
    "simon.lindgren",
    "harald.nordgren",
    "jesper.roth",
    "robert.gionea",
]

for username in users:
    jql = "status=done AND createdDate>=\"{0}\" AND assignee = {1}".format(
        start_date,
        username,
    )
    resp = requests.post(
        "https://betalo.atlassian.net/rest/api/2/search",
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        json={
            "jql": jql,
            "maxResults": 0,
        },
    )
    if resp.status_code != 200:
        print(resp)
        print(resp.json())
        sys.exit(1)

    json_resp = resp.json()
    counter[username] = json_resp["total"]

total_prs = sum(counter.values())
ratios = {username: prs/total_prs for username, prs in counter.items()}
sorted_ratios = sorted(ratios.items(), reverse=True, key=lambda kv: kv[1])

result = []
for ratio_tuple in sorted_ratios:
    username, ratio = ratio_tuple
    result.append((username, "{0:.0%}".format(ratio)))

print()
print("Completed JIRA tasks since {0}:".format(start_date))
pprint.pprint(result)

