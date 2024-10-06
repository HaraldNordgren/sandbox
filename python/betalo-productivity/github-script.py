A. Commit message:
Add timeout to HTTP requests in user fetching script

B. Change summary:
Added a `timeout` parameter to the HTTP GET requests in order to prevent potential Denial of Service (DoS) caused by uncontrolled resource consumption when connections are left open indefinitely.

C. Compatibility Risk:
Low

D. Fixed Code:
```python
#!/usr/bin/env python3

import os
import pprint
import requests
import sys

from ratios import Ratio

TOKEN = os.environ.get('GITHUB_OAUTH_TOKEN', "")

if TOKEN == "":
    print("Please set environment variable GITHUB_OAUTH_TOKEN.")
    print()
    print("Go to 'https://github.com/settings/tokens' and generate a token with 'repo' accces ('Full control of private repositories') then",)
    print()
    print("    export GITHUB_OAUTH_TOKEN='token'")
    sys.exit(1)

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
    resp = requests.get(u, headers=HEADERS, timeout=10)
    if resp.status_code != 200:
        print(resp)
        sys.exit(1)

    json_resp = resp.json()
    counter[username] = json_resp["total_count"]

result = Ratio.calculate_ratios(counter)
print()
print("Merged Betalo pull requests since {0}:".format(start_date))
pprint.pprint(result)
```
