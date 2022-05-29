#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from . import bashutil
from .bashutil import sh, run
import subprocess

_HOME_DIR = os.path.expanduser('~')


class Attacker:
    def __init__(self, hashformat, wordlist, infile, hashpath, args=None):
        if args is None:
            args = {}
        self.hashformat = hashformat
        self.wordlist = wordlist
        self.infile = infile
        self.hashpath = hashpath
        self.args = args

    def tohash(self):
        """calc input file hash"""
        pass

    def crack(self):
        """run crack"""
        pass

    def show_result(self):
        """show crack result"""
        pass

    def pwdpath(self):
        """password store file"""
        pass

    def clean(self):
        """clean password file, be careful, it will delete all cracked result!"""
        pass


class Hashcat(Attacker):
    """Hashcat"""

    def __init__(self, hashformat, wordlist, infile, hashpath, args=None):
        if args is None:
            args = {}
        super().__init__(hashformat, wordlist, infile, hashpath, args)

    def tohash(self):
        super(Hashcat, self).tohash()
        run("%s %s > %s" %
            (bashutil.perllib('7z2hashcat'), self.infile, self.hashpath))

    def crack(self):
        super(Hashcat, self).crack()
        hashcat_dir = os.listdir('/usr/local/Cellar/hashcat')
        if hashcat_dir and len(hashcat_dir) > 0:
            opencl_dir = os.path.join('/usr/local/Cellar/hashcat', hashcat_dir[0], 'share/hashcat/OpenCL')
            print("change to opencl_dir: %s" % (opencl_dir))
            os.chdir(opencl_dir)
        else:
            print("Can not found hashcat dir")
        subprocess.call("hashcat -a 0 -m 11600 %s %s" %
                        (self.hashpath, self.wordlist), shell=True)

    def show_result(self):
        super(Hashcat, self).show_result()
        result = sh("hashcat --show %s" % (self.hashpath))
        if 'length exception' in result:
            print('error, manual show pwd...')
            result = sh("cat %s | grep '%s'" %
                        (self.pwdpath(), self.hashformat))
        return result

    def pwdpath(self):
        super(Hashcat, self).pwdpath()
        return os.path.join(_HOME_DIR, '.hashcat', 'hashcat.potfile')

    def clean(self):
        super(Hashcat, self).clean()
        bashutil.rm(self.pwdpath())
        bashutil.rm(self.hashpath)


class JTR(Attacker):
    """JohnTheRipper"""

    def __init__(self, hashformat, wordlist, infile, hashpath, args=None):
        if args is None:
            args = {}
        super().__init__(hashformat, wordlist, infile, hashpath, args)

    def tohash(self):
        super(JTR, self).tohash()
        run("%s %s > %s" %
            (bashutil.perllib('7z2john'), self.infile, self.hashpath))

    def crack(self):
        super(JTR, self).crack()
        # for print status when Press Ctrl-C
        subprocess.call("john --wordlist=%s --encoding=UTF-8 %s" %
                        (self.wordlist, self.hashpath), shell=True)

    def show_result(self):
        super(JTR, self).show_result()
        return sh("john --show %s" % (self.hashpath))

    def pwdpath(self):
        super(JTR, self).pwdpath()
        return os.path.join(_HOME_DIR, '.john', 'john.pot')

    def clean(self):
        super(JTR, self).clean()
        bashutil.rm(self.pwdpath())
        bashutil.rm(self.hashpath)
