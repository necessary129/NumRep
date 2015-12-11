#!/usr/bin/env python

# Copyright (c) 2015 Muhammed Shamil K
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from __future__ import print_function

import sys

def testmod(mod):
    import doctest
    mod = __import__(mod)
    err, test = doctest.testmod(m=mod,verbose=True)
    if err > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    import os
    first = testmod('NumRep')
    if not first:
        sys.exit(1)
    for mod in os.listdir('NumRep'):
        if mod.startswith('__') or mod.endswith('.pyc'):
            continue
        module = 'NumRep.'+mod.replace('.py','')
        test = testmod(module)
        if not test:
            sys.exit(1)
