#!/usr/bin/python
# -*- coding: utf-8 -*-

from module import read_from_json
import re

lines = read_from_json('イギリス').split("\n")

for line in lines:
    category = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category is not None:
        print (category.group(1))
