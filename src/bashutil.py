#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import io
import argparse
import subprocess

_ROOT_PATH = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.path.pardir))


def run(command):
    print(command + '...')
    subprocess.run(command, shell=True)


def sh(command, print_msg=True):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    if print_msg:
        print(result)
    return result


def perllib(name):
    path = os.path.join(_ROOT_PATH, 'src', name)
    return "%s.exe" % (path) if os.name == 'nt' else "%s.pl" % (path)


def hasexec(cmd):
    result = sh("%s --version" % (cmd), print_msg=False)
    return ('not found' not in result)


def ischina():
    result = os.system('ping www.google.com -t 3 -l 1')
    return (result is True)


def rm(path):
    if os.path.exists(path):
        os.remove(path)
