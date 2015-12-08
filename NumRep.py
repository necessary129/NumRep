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

"""
This module provides a class to represent the place vaues in a given number, eg:
    >>> a = NumRep(1234456789123)
    >>> a
    NumRep(Crores=123445,Lakhs=67,Thousands=89,Hundreds=1,Tens=2,Ones=3)
    >>> a.crores
    123445
    >>> a.ones
    3

    This raises TypeError when you give a non-number to it.
    eg:
    >>> a = NumRep('notanumber123')
    Traceback (most recent call last):
      ...
    TypeError: Not a valid number

    This class also provides an all() function, which gives you the real value of the given denomination, 
    eg:
    >>> a = NumRep(1234456789123)
    >>> a.all(HUNDREDS)
    12344567891
"""

HUNDREDS = 'hundreds'
THOUSANDS = 'thousands'
TENS = 'tens'
ONES = 'ones'
LAKHS = 'lakhs'
CRORES = 'crores'

class RepNum(int):
    def GetRep(self):
        return NumRep(self)
    def __sub__(self, other):
        ret = int(self).__sub__(other)
        return RepNum(ret)
    def __add__(self, other):
        ret = int(self).__add__(other)
        return RepNum(ret)
    def __neg__(self):
        ret = int(self).__neg__()
        return RepNum(ret)
    def __mul__(self, other):
        ret = int(self).__mul__(other)
        return RepNum(ret)
    def __floordiv__(self, other):
        ret = int(self).__floordiv__(other)
        return RepNum(ret)
    def __truediv__(self, other):
        ret = int(self).__truediv__(other)
        return RepNum(ret)
    def __mod__(self, other):
        ret = int(self).__mod__(other)
        return RepNum(ret)
    def __divmod__(self, other):
        ret = int(self).__divmod__(other)
        return RepNum(ret)
    def __pos__(self):
        ret = int(self).__pos__()
        return RepNum(ret)
    def __abs__(self):
        ret = int(self).__abs__()
        return RepNum(ret)
    def __rsub__(self, other):
        ret = int(self).__rsub__(other)
        return RepNum(ret)
    def __radd__(self, other):
        ret = int(self).__radd__(other)
        return RepNum(ret)
    def __rmul__(self, other):
        ret = int(self).__rmul__(other)
        return RepNum(ret)


class NumRep(object):
    """
    This class provides a way to represent the place values in a given number, eg:
    >>> a = NumRep(1234456789123)
    >>> a
    NumRep(Crores=123445,Lakhs=67,Thousands=89,Hundreds=1,Tens=2,Ones=3)
    >>> a.crores
    123445
    >>> a.ones
    3
    >>> a.hundreds
    1
    >>> a.tens
    2
    >>> a.lakhs
    67

    And Every integer in the NumRep has a GetRep() method, which returns the Representation of the number itself,
    eg:
    >>> a = NumRep(123456789)
    >>> a
    NumRep(Crores=12,Lakhs=34,Thousands=56,Hundreds=7,Tens=8,Ones=9)
    >>> a.crores
    12
    >>> a.crores.GetRep()
    NumRep(Tens=1,Ones=2)
    >>> a.crores.GetRep().tens.GetRep()
    NumRep(Ones=1)

    You can also do arithmetic operations on them and then use GetRep()
    eg:
    >>> a = NumRep(123456789)
    >>> a
    NumRep(Crores=12,Lakhs=34,Thousands=56,Hundreds=7,Tens=8,Ones=9)
    >>> (a.crores - 2).GetRep()
    NumRep(Tens=1)

    This raises TypeError when you give a non-number to it.
    eg:
    >>> a = NumRep('notanumber123')
    Traceback (most recent call last):
      ...
    TypeError: Not a valid number

    This class also provides an all() function, which gives you the real value of the given denomination, 
    eg:
    >>> a = NumRep(1234456789123)
    >>> a.all('hundreds')
    12344567891
    >>> a.all(HUNDREDS)
    12344567891

    """
    __lens = lens = dict(
    lakhs=5,
    crores =7,
    thousands = 3,
    hundreds = 2,
    tens = 1,
    ones = 9,
    )
    def __init__(self, num):
        try:
            num = RepNum(num)
        except Exception:
            raise TypeError("Not a valid number")
        self.number = RepNum(num)
        self.crores = RepNum(0)
        self.lakhs = RepNum(0)
        self.thousands = RepNum(0)
        self.hundreds = RepNum(0)
        self.tens = RepNum(0)
        self.ones = RepNum(0)
        for time in range(1,9):
            mod = num % 10
            if time == 1:
                self.ones = RepNum(mod)
            if time == 2:
                self.tens = RepNum(mod)
            if time == 3:
                self.hundreds = RepNum(mod)
            if time == 4:
                thou = RepNum(mod)
            if time == 5:
                self.thousands = RepNum(thou + (mod*10))
            if time == 6:
                lak = RepNum(mod)
            if time == 7:
                self.lakhs = RepNum(lak + (mod*10))
            if time == 8:
                self.crores = RepNum(num)
            num -= mod
            num = num/10
        li = []
        if self.crores:
            li.append("Crores={0}".format(self.crores))
        if self.lakhs:
            li.append("Lakhs={0}".format(self.lakhs))
        if self.thousands:
            li.append("Thousands={0}".format(self.thousands))
        if self.hundreds:
            li.append("Hundreds={0}".format(self.hundreds))
        if self.tens:
            li.append("Tens={0}".format(self.tens))
        if self.ones:
            li.append("Ones={0}".format(self.ones))
        self.__li = li
    def all(self, digit):
        """
        This function returns the original value of the specified denomination in the number specified,
        not the value in the place.
        eg:
        >>> a = NumRep(1234456789123)
        >>> a.all('hundreds')
        12344567891
        >>> a.all('tens')
        123445678912
        >>> a.all('lakhs')
        12344567
        >>> a.all('crores')
        123445
        >>> a.all(CRORES)
        123445
        
        etc.

        """
        gth = self.__lens.get(digit, None)
        if not gth:
            raise TypeError("Not a valid denomination")
        sr = str(self.number)
        if gth == 9:
            return RepNum(sr)
        return RepNum(sr[:(-gth)])

    def __repr__(self):
        return "NumRep({0})".format(",".join(self.__li))

if __name__ == '__main__':
    import sys
    PY2 = sys.version[0] == "2"
    try:
        while True:
            num = None
            try:
                if PY2:
                    num = int(raw_input("Type the number you want to convert: "))
                else:
                    num = int(input("Type the number you want to convert: "))
            except ValueError:
                print('Not a valid Number')
                continue
            if num:
                print(NumRep(num))
            else:
                sys.exit(0)
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)

