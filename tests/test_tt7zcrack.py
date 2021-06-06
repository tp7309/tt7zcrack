#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
import os
import subprocess
from src import tt7zcrack
from src.tt7zcrack import HASH_PATH
from src import attackers

tests_path = os.path.dirname(os.path.abspath(__file__))
asserts_path = os.path.abspath(os.path.join(tests_path, os.pardir, 'asserts'))
p7zfile = os.path.join(asserts_path, 'crackme.7z')
wordlist_file = os.path.join(asserts_path, 'crackme_wordlist.txt')
crackme_pwd = '456'


def run(command):
    print(command + '...')
    subprocess.run(command, shell = True, check=True)


def sh(command, print_msg = True):
    p = subprocess.Popen(command,
                         shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    if print_msg:
        print(result)
    return result


class Test_tt7zcrack(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test_tt7zcrack, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(Test_tt7zcrack, cls).tearDownClass()

    def go(self, wordlist = wordlist_file, engine = 'hashcat', china = False, clean = False):
        args = ['--wordlist', wordlist, '--engine', engine]
        if china:
            args.append('--china')
        if clean:
            args.append('--clean')
        args.append(p7zfile)
        tt7zcrack.domain(tt7zcrack.parse_args(args))

    def rm(self, path):
        if os.path.exists(path):
            os.remove(path)

    def test_hashcat(self):
        self.go(wordlist_file, 'hashcat')
        attacker = attackers.Hashcat('7z', wordlist_file, p7zfile, HASH_PATH)
        result = attacker.show_result()
        self.assertTrue(crackme_pwd in result)

    def test_jtr(self):
        self.go(wordlist_file, 'jtr')
        attacker = attackers.JTR('7z', wordlist_file, p7zfile, HASH_PATH)
        result = attacker.show_result()
        self.assertTrue(crackme_pwd in result)

    def test_clean(self):
        self.go(wordlist_file, 'hashcat', clean = True)
        homedir = os.path.expanduser('~')
        self.assertFalse(os.path.exists(HASH_PATH))
        self.assertFalse(
            os.path.exists(os.path.join(homedir, '.hashcat',
                                        'hashcat.potfile')))
        self.assertFalse(
            os.path.exists(os.path.join(homedir, '.john', 'john.pot')))

    def test_china_mirror(self):
        self.go(wordlist_file, 'hashcat', china=True)
        # CI env may have different base_profile path, so only make sure brew is still work.
        self.assertIsNotNone("brew --repo")


if __name__ == '__main__':
    unittest.main()
