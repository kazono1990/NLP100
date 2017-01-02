#!/usr/bin/python
# -*- coding: utf-8 -*-

from module import read_from_json
import re
import requests
import json


# 階層型の dict をフラットにする
def flatten(input_dict):
    ret_dict = {}
    for k, v in input_dict.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(flatten(e))
        elif isinstance(v, dict):
            ret_dict.update(flatten(v))
        else:
            ret_dict[k] = v
    return ret_dict

def remove_markup(line):
    line = re.sub(r"'{2,5}", r"", line)
    line = re.sub(r"\[\[(.+?)\]\]", r"\1", line)
    line = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", line)
    line = re.sub(r"<.*?>", r"", line)
    line = re.sub(r"\[.*?\]", r"", line)
    return line

tmp_dict = {}
lines = re.split(r'\n[\|}]', read_from_json('イギリス'))

for line in lines:
    tmp_line = re.search("^(.*?)\s=\s(.*)", line, re.DOTALL)
    if tmp_line is not None:
        tmp_dict[tmp_line.group(1)] = remove_markup(tmp_line.group(2))

url = 'https://en.wikipedia.org/w/api.php'
payload = {"action": "query",
           "titles": "File:{}".format(tmp_dict['国旗画像']),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

json_data = requests.get(url, params=payload).json()
print (flatten(json_data)['url'])
