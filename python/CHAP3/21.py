#!/usr/bin/python
# -*- coding: utf-8 -*-

from module import read_from_json

lines = read_from_json('イギリス').split("\n")

for line in lines:
    if 'Category' in line:
        print(line)

# python 3 ならこっちでも ok (リスト表示で出力される)
# print ([line for line in lines if 'Category' in line])
