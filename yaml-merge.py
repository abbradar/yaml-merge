#!/usr/bin/env python3

import sys
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


# Mutating recursive dictionary merge
def merge(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        for k, v in b.items():
            if k in a:
                a[k] = merge(a[k], v)
            else:
                a[k] = v
        return a
    else:
        return b


def load_file(name):
    with open(name) as f:
        return yaml.load(f, Loader=Loader)


file_names = sys.argv[1:]
files = [load_file(name) for name in file_names]
result = {}
for data in files:
    result = merge(result, data)
print(yaml.dump(result, Dumper=Dumper))
