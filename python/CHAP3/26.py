#!/usr/bin/python
# -*- coding: utf-8 -*-

from module import read_from_json
import re

tmp_dict = {}
lines = re.split(r'\n[\|}]', read_from_json('イギリス'))

for line in lines:
    tmp_line = re.search("^(.*?)\s=\s(.*)", line, re.DOTALL)
    if tmp_line is not None:
        tmp_dict[tmp_line.group(1)] = re.sub(r"'{2,5}", r"", tmp_line.group(2))

for k, v in sorted(tmp_dict.items(), key=lambda x: x[1]):
    print(k, v)
