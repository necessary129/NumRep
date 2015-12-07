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

import setup
vre = setup.vre

def write_version(fl,vrs):
    for x,y in enumerate(vrs):
        vrs[x] = str(y)
    vers = ".".join(vrs)
    version = "Version: {0}".format(vers)
    fl = vre.sub(version,fl)
    return fl

def do():
    readme = setup.read_file('README.rst')
    version = setup.getversion()
    version[-1] += 1
    new = write_version(readme,version)
    with open('README.rst','w') as f:
        f.write(new)

if __name__ == '__main__':
    do()