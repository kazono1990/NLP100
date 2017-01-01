#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1]) as f:
    file = f.read()

print (file.replace('\t', ' '))
