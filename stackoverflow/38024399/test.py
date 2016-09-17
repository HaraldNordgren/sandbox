#!/usr/bin/env python3

f = open('data')

err_dict = {k: [] for k in ['p','v','s','T']}

i = 0
for line in f:
    i += 1
    if i < 8:
        continue

    if line.startswith("POINT "):
        continue

    line_split = line.split()
    err_dict[line_split[0]].append(line_split[3])

print(err_dict['p'])
