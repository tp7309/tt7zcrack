# tt7zcrack

[![Build Status](https://travis-ci.org/tp7309/tt7zcrack.svg?branch=master)](https://travis-ci.org/tp7309/tt7zcrack)
[![Coverage Status](https://coveralls.io/repos/github/tp7309/tt7zcrack/badge.svg?branch=master)](https://coveralls.io/github/tp7309/tt7zcrack?branch=master)

首先 tt7zcrack 是一个支持 GPU/CPU 加速的 7z 破解工具，速度比用`7z`解压命令一个个试验要快很多。写这个小工具的原因是作者君的一个 7z 压缩包密码忘了，在破解过程中遇到了不少坑，现有的工具有一定的学习成本，所以把这些结果输出供有碰到相同问题的同学使用。

# 使用要求

Python 3.5 或之后版本，没用过 python 的没关系，看下面教程安装一个即可。
[python 安装教程](https://www.runoob.com/python3/python3-install.html)

# 安装

`tt7zcrack` 可以使用 Python 的`pip`轻松安装::

```
pip install tt7zcrack
```

# 快速开始

## Mac

确保[brew](https://brew.sh/index_zh-cn)已安装。

```bash
# pwds.txt中存放可能的密码列表，可以使用`ttpassgen`来生成，注意文件最好是使用`utf-8`编码。
# crack.7z换成你要破解的7z文件。
tt7zcrack --wordlist pwds.txt crack.7z
```

当破解程序运行完成后，会下类似下图的显示，图中**456**就是密码了:
![image](https://github.com/tp7309/tt7zcrack/blob/master/asserts/result.png)

## Linux/Windows

当前未支持，添加中。

# 详情使用

```bash
tt7zcrack --help
usage: tt7zcrack.py [-h] [--wordlist [WORDLIST]] [--engine {hashcat,jtr}] [--clean] [file]

7z GPU/CPU crack tool

positional arguments:
  file                  要破解的7z文件 (default: None)

optional arguments:
  -h, --help            显示帮助
  --wordlist [WORDLIST]
                        供猜解的密码列表，可以手动写，也可以使用`ttpassgen`来生成，编译最好是"utf-8"
                        (default: '')
  --engine {hashcat,jtr}
                        密码破解工具(default: hashcat)
  --clean               清除本地保存的已破解密码文件 (默认: False)
```

如果默认的出错(如不能生成 hash)时可以换`jtr`试试。

已破解的密码会被密码破解工具保存在本地供查询，使用下面命令可以删除，注意这会删除所有已破解结果！

```bash
tt7zcrack --clean
```

# 7z 命令(供参考)

```bash
# Mac上安装7z，Windows直接下载然后配置环境变量
brew install p7zip

# 创建带密码7z压缩包
7z a -p456 test.7z test.txt
# 解压缩带密码7z压缩包
7z x -p456 test.7z

# 创建无密码7z压缩包
7z a test.7z test.txt
# 解压缩无密码7z压缩包
7z x test.7z
```

# Thanks

[7zhashcat](https://github.com/philsmd/7z2hashcat)
