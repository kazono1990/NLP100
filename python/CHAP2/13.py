#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('col1.txt') as f1, open('col2.txt') as f2:
    line1, line2 = f1.readlines(), f2.readlines()

with open('merge.txt', 'w') as f:
    for col1, col2 in zip(line1, line2):
        f.write("\t".join([col1.rstrip(), col2]))
