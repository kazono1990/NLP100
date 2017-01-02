#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

def read_from_json (title=''):
    with open("jawiki-country.json") as f:
        json_file = f.readline()
        while json_file:
            article = json.loads(json_file)
            if article['title'] == title:
                return article['text']
            else:
                json_file = f.readline()
    return ""
