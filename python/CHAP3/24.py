#!/usr/bin/python
# -*- coding: utf-8 -*-

from module import read_from_json
import re

lines = read_from_json('イギリス').split("\n")

for line in lines:
    media = re.search("^\[\[(File|ファイル):(.*?)\|", line)
    if media is not None:
        print (media.group(2))
