#!/usr/bin/env python
# coding: utf-8
# By Sandaru Ashen: https://github.com/Sl-Sanda-Ru,https://t.me/Sl_Sanda_Ru

import os
import sys

PYTHON_VERSION = '.'.join(str(i) for i in sys.version_info[:2])

if PYTHON_VERSION not in ('3.8', '3.9', '3.10','3.11'):
    print('\x1b[1m\x1b[91m [!] Your Python Version Is Not Supported'.center(os.get_terminal_size().columns))
    exit('\x1b[1m\x1b[91m [!] Please Update Your Python'.center(os.get_terminal_size().columns))
if os.name == 'nt':
    os.system('python .{}.py'.format(PYTHON_VERSION))
else:
    os.system('python{} .{}.py'.format(PYTHON_VERSION, PYTHON_VERSION))
