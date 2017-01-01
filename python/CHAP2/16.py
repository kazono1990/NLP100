#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def split_file(f_name, number_of_sections):
    with open(f_name) as f:
        lines = f.readlines()

    if len(lines) % number_of_sections != 0:
        raise Exception("File can't divide by N=%d" % number_of_sections)
    else:
        number_of_lines = len(lines) / number_of_sections

    for i in range(number_of_sections):
        print ("aaa")
        with open("split%s.txt" % str(i), 'w') as output:
            output.writelines(lines[int(number_of_lines) * i: int(number_of_lines) * (i + 1)])

if __name__ == '__main__':
    try:
        split_file(sys.argv[1], int(sys.argv[2]))
    except Exception as err:
        print("Error:", err)
