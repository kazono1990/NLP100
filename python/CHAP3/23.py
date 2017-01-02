#!/usr/bin/python
# -*- coding: utf-8 -*-

from module import read_from_json
import re

lines = read_from_json('イギリス').split("\n")

for line in lines:
    section = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if section is not None:
        print(section.group(2), len(section.group(1)) - 1)
