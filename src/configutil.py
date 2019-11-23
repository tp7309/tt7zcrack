#!/usr/bin/python
# -*- coding:utf-8 -*-


import io
import json


class CrackConfig(object):
    def __init__(self, d):
        pass


def read_config(src):
    config = None
    with io.open(src, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config


def write_config(config, dest):
    with io.open(dest, 'w', encoding='utf-8') as f:
        json.dump(config, f, sort_keys=True, indent=4, ensure_ascii=False)
