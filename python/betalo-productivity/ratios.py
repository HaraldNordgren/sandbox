#!/usr/bin/env python

def redact(username):
    if username != "harald.nordgren" and username != "haraldnordgren":
        return "REDACTED"
    return username

class Ratio:
    def calculate_ratios(counter):
        total_prs = sum(counter.values())

        ratios = {}
        for username, prs in counter.items():
            ratios[username] = {
                "total": prs,
                "ratio": prs/total_prs,
            }
        
        sorted_ratios = sorted(
            ratios.items(),
            reverse=True,
            key=lambda kv: kv[1]["ratio"],
        )
        
        result = []
        for ratio_tuple in sorted_ratios:
            username, ratio = ratio_tuple
            result.append((redact(username), "{0} ({1:.1%})".format(
                ratio["total"],
                ratio["ratio"],
            )))

        return result

