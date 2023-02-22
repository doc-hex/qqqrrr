#!/usr/bin/env python
import os, sys, pyqrcode

p = ' '.join(sys.argv[1:])
if not p:
    print(f'{sys.argv[0]} data-for-qr')
    sys.exit(1)

q = pyqrcode.create(p)
print(q.terminal())

