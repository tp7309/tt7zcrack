#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import subprocess

_ROOT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))


def run(command):
    print(command + '...')
    subprocess.run(command, shell=True)


def sh(command, print_msg=True):
    p = subprocess.Popen(command,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    result = p.stdout.read()
    try:
        result = result.decode('utf-8')
    except UnicodeDecodeError:
        result = result.decode('gbk')
    if print_msg:
        print(result)
    return result


def isci():
    return os.environ.get('CI') in ['True', 'true', '1']


def perllib(name):
    path = os.path.join(_ROOT_PATH, 'src', name)
    if os.name == 'nt':
        return "%s.exe" % (path)
    else:
        perl = 'perl'
        return "%s %s.pl" % (perl, path)


def hasexec(cmd):
    result = sh("%s --version" % (cmd), print_msg=False)
    return not ('not found' in result or u'不是' in result)


def ischina():
    if isci():
        return False
    result = os.system('ping www.google.com -t 3 -c 1')
    return result > 0


def rm(path):
    if os.path.exists(path):
        os.remove(path)
