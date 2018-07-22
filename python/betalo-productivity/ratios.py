#!/usr/bin/env python

class Ratio:
    def calculate_ratios(counter):
        total_prs = sum(counter.values())
        ratios = {username: prs/total_prs for username, prs in counter.items()}
        sorted_ratios = sorted(ratios.items(), reverse=True, key=lambda kv: kv[1])
        
        result = []
        for ratio_tuple in sorted_ratios:
            username, ratio = ratio_tuple
            result.append((username, "{0:.0%}".format(ratio)))

        return result

