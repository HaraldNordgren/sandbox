#!/usr/bin/env python

def flatten(lst):

    result = []

    def traverse(lst):
        if isinstance(lst, list):
            for sublist in lst:
                traverse(sublist)
        else:
            result.append(lst)

    traverse(lst)
    return result
