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

def calc(conv):
    def dec(cls):
        funcs = ['__add__','__sub__','__mul__','__radd__','__rsub__','__rmul__','__floordiv__',
        '__truediv__','__mod__','__divmod__','__eq__','__le__','__lt__','__gt__','__ge__','__ne__']
        for f in funcs:
            def func(fff):
                def gen(self, other):
                    ret = getattr(conv(self),fff)(other)
                    return cls(ret)
                return gen
            setattr(cls, f, func(f))
        return cls
    return dec

def abpos(conv):
    def dec(cls):
        funcs = ['__neg__','__pos__','__abs__']
        for f in funcs:
            def func(f):
                def gen(self):
                    ret = getattr(conv(self),f)()
                    return cls(ret)
                return gen
            setattr(cls, f, func(f))
        return cls
    return dec

@abpos(int)
@calc(int)
class RepNum(int):
    def GetRep(self):
        return NumRep(self)