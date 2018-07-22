#!/usr/bin/env python3

import pprint
import requests
import sys

from ratios import Ratio
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
    jql = "status=done AND resolved>=\"{0}\" AND assignee={1}".format(
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

result = Ratio.calculate_ratios(counter)
print()
print("Completed JIRA tasks since {0}:".format(start_date))
pprint.pprint(result)

