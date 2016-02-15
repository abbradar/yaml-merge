#!/usr/bin/env python

import sys
import yaml

# Mutating recursive dictionary merge
def merge(from, to):
  if isinstance(from, dict) and isinstance(to, dict):
    for k, v in from.iteritems():
      if k in to:
        to[k] = merge(v, to[k])
      else:
        to[k] = v
    return to
  else:
    return from

if len(sys.argv) < 3:
  sys.exit("Usage: yaml-merge.py file1.yaml file2.yaml")

file1_name = sys.argv[1]
file2_name = sys.argv[2]

# Either I don't know a better way, or Python gets ugly...
file1 = None
with open(file1_name) as f:
  file1 = yaml.load(f)

file2 = None
with open(file2_name) as f:
  file2 = yaml.load(f)

result = merge(file1, file2)

print(yaml.dump(result))
