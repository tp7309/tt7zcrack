# tt7zcrack

[![Build Status](https://travis-ci.org/tp7309/tt7zcrack.svg?branch=master)](https://travis-ci.org/tp7309/tt7zcrack)
[![Coverage Status](https://coveralls.io/repos/github/tp7309/tt7zcrack/badge.svg?branch=master)](https://coveralls.io/github/tp7309/tt7zcrack?branch=master)

README i18n: [中文说明](https://github.com/tp7309/tt7zcrack/blob/master/README_zh_CN.md)

Fast 7zip crack assistant tool which support GPU/CPU.

# Requirements

Python 3.5 or later.
[python install](https://www.runoob.com/python3/python3-install.html)

# Install

`TTPassGen` can be easily installed using pip:

```
pip install tt7zcrack
```

# Quick Start

## Mac

make sure [brew](https://brew.sh/index_zh-cn) is installed.

```bash
# use passwords from pwds.txt to crack file
tt7zcrack --wordlist pwds.txt crack.7z
```

when crack is completed, password will be shown like this:
![image](https://github.com/tp7309/tt7zcrack/blob/master/asserts/result.png)

## Linux/Windows

Currently not supported.

# Usage

```bash
tt7zcrack --help
usage: tt7zcrack.py [-h] [--wordlist [WORDLIST]] [--engine {hashcat,jtr}] [--clean] [file]

7z GPU/CPU crack tool

positional arguments:
  file                  7z file path (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --wordlist [WORDLIST]
                        wordlist dict path, you can use 'ttpaasgen' to
                        generate. (default: )
  --engine {hashcat,jtr}
                        password recovery engine (default: hashcat)
  --clean               clean related secure files (default: False)
```

if the hash file cannot generated correctly, you can use `jtr` engine to try again.

The cracked password will be saved locally by the password cracking tool for next query. Use the following command to delete it. Note that this will delete all cracked results!

```bash
tt7zcrack --clean
```

# 7z commands

```bash
# install 7z on Mac
brew install p7zip

# compress with password
7z a -p456 test.7z test.txt
# extract with password
7z x -p456 test.7z

# compress without password
7z a test.7z test.txt
# extract without password
7z x test.7z
```

# Thanks

[7zhashcat](https://github.com/philsmd/7z2hashcat)
