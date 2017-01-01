#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

prefs = set()

with open(sys.argv[1]) as f:
    line = f.readline()
    while line:
        prefs.add(line.split()[0])
        line = f.readline()

for pref in prefs:
    print (pref)
