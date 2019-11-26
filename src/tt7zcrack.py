#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Fast 7zip crack assistant tool which support GPU/CPU.
@poject: tt7zcrack
@auther: tp7309
'''

import os
import sys
import argparse
from enum import Enum
from . import bashutil
from .bashutil import sh, run
from . import attackers

_ROOT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))
SRC_DIR = os.path.join(_ROOT_PATH, 'src')
_CACHE_DIR = os.path.join(_ROOT_PATH, 'cache')
HASH_PATH = 'ttcrack_hash.txt'


class Engine(Enum):
    hashcat = 'hashcat'
    jtr = 'jtr'

    def __str__(self):
        return self.value


def set_china_mirror():
    # Homebrew repo mirror
    run('git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git'
        )
    run('git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git'
        )
    run('git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git'
        )
    run('brew update')
    if not os.environ.get('HOMEBREW_BOTTLE_DOMAIN'):
        run("echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.bash_profile"
            )
        run('source ~/.bash_profile')


def isinstalled():
    return bashutil.hasexec('hashcat') and bashutil.hasexec('john')


def install_osx(force_china):
    if not bashutil.hasexec('brew'):
        print('please install brew!')
        return
    if force_china or bashutil.ischina():
        set_china_mirror()
    run('brew install p7zip')
    run('brew install hashcat')
    run('brew install john-jumbo')
    # 7z2john.pl dependencies
    print("we need sudo to install perl script dependencies...")
    run("curl -L https://cpanmin.us | perl - --sudo App::cpanminus && sudo cpanm Compress::Raw::Lzma")
    if not isinstalled():
        print('\n\ninstall failed!')
    else:
        print('\n\ninstall done, please rerun command')


def parse_args(args):
    parser = argparse.ArgumentParser(
        description='7z GPU/CPU crack tool',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--wordlist',
        nargs='?',
        default='',
        help="wordlist dict path, you can use 'ttpaasgen' to generate.")
    parser.add_argument('--engine',
                        default='hashcat',
                        type=Engine,
                        choices=list(Engine),
                        help='password recovery engine')
    parser.add_argument('--china',
                        action='store_true',
                        default=False,
                        help='force use china mirror for brew、pip')
    parser.add_argument('--clean',
                        action='store_true',
                        default=False,
                        help='clean related secure files')
    parser.add_argument('file', nargs='?', help='7z file path')
    return parser.parse_args(args)


def doclean(args):
    attackers.Hashcat('7z', args.wordlist, args.file, HASH_PATH).clean()
    attackers.JTR('7z', args.wordlist, args.file, HASH_PATH).clean()
    print('clean done')


def domain(args):
    if not args.clean and not args.wordlist:
        print("please input wordlist dict path")
        return

    if not isinstalled():
        if sys.platform == 'darwin':
            install_osx(args.china)
        else:
            print('currently only support "MacOS"!')
            return
    if args.engine == Engine.hashcat:
        # use hashcat
        attacker = attackers.Hashcat('7z', args.wordlist, args.file, HASH_PATH)
    elif args.engine == Engine.jtr:
        # use JohnTheRipper
        attacker = attackers.JTR('7z', args.wordlist, args.file, HASH_PATH)
    else:
        print('error engine!')
    if args.clean:
        doclean(args)
        return
    attacker.tohash()
    attacker.crack()
    print('crack result'.center(100, '-'))
    attacker.show_result()


def main():
    domain(parse_args(sys.argv[1:]))


if __name__ == "__main__":
    main()
