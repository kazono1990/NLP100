#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

with open('jawiki-country.json') as f:
    json_file = f.readline()
    while json_file:
        article = json.loads(json_file)
        if article['title'] == 'イギリス':
            print (article['text'])
        json_file = f.readline()
