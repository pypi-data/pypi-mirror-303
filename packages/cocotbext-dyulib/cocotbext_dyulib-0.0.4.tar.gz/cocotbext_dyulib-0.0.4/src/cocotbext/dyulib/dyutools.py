"""Main module."""
import os
import re


def find_all(name, path):
    '''Returnes a list of files with exact name match at path and its subfolders'''
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def find_all_match(pattern, path):
    '''Returnes a list of files with pattern match at path and its subfolders'''
    result = []
    for root, dirs, files in os.walk(path):
        for name in [x for x in files if re.match(pattern)]:
            result.append(os.path.join(root, name))
    return result
