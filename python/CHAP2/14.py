#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines[:int(sys.argv[2])]:
    print (line.rstrip())
