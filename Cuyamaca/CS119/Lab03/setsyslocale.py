#!/usr/bin/env python3

# Lab3ex1

import platform
import locale

if platform.system().startswith('Windows'):
    locale.setlocale(locale.LC_ALL, 'en-US') # PC
else:
    locale.setlocale(locale.LC_ALL, 'en_US') # Mac/Linux/...and
