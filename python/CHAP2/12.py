#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def get_col(src, c_number, f_name):
    column = []
    for line in src:
        column.append(line.split()[c_number] + "\n")
    with open(f_name, 'w') as f:
        f.writelines(column)

with open(sys.argv[1]) as f:
    lines = f.readlines()

get_col(lines, 0, 'col1.txt')
get_col(lines, 1, 'col2.txt')
