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

from .utils import abpos, calc

@abpos(int)
@calc(int)
class RepNum(int):
    def GetRep(self):
        return NumRep(self)

@abpos(int)
@calc(int)
class NumRep(int):
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
        >>> print(a)
        123445 Crores, 67 Lakhs, 89 Thousands, 1 Hundred, 2 Tens, 3 Ones

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

    You can compare and do arithmetic operations NumReps with integers and also with other NumReps, like:
        >>> c = NumRep(15)
        >>> c
        NumRep(Tens=1,Ones=5)
        >>> c + 10
        NumRep(Tens=2,Ones=5)
        >>> b = NumRep(10)
        >>> b
        NumRep(Tens=1)
        >>> c + b
        NumRep(Tens=2,Ones=5)

    This raises TypeError when you give it an invalid number, eg:
        >>> a = NumRep('notanumber1111')
        Traceback (most recent call last):
        ...
        TypeError: Not a valid Number.

    You can also do arithmetic operations on them and then use GetRep()
    eg:
        >>> a = NumRep(123456789)
        >>> a
        NumRep(Crores=12,Lakhs=34,Thousands=56,Hundreds=7,Tens=8,Ones=9)
        >>> (a.crores - 2).GetRep()
        NumRep(Tens=1)


    This class also provides an all() function, which gives you the real value of the given denomination, 
    eg:
        >>> a = NumRep(1234456789123)
        >>> a.all('hundreds')
        12344567891
        >>> a.all(HUNDREDS)
        12344567891


    """
    _lens = dict(
    lakhs=5,
    crores =7,
    thousands = 3,
    hundreds = 2,
    ones = 9,
    )
    _ones = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : 'eight',
        9 : 'nine'
        }
    def __new__(self, num):
        r = False
        try:
            a = int(num)
        except Exception as e:
            r = True
        if r:
            raise TypeError("Not a valid Number.")
        return int.__new__(self, num)
    def __init__(self, num):
        num = RepNum(num)
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
        self._li = li
        super(NumRep, self).__init__()
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
        gth = self._lens.get(digit, None)
        if not gth:
            raise TypeError("Not a valid denomination")
        sr = str(self.number)
        if gth == 9:
            return RepNum(sr)
        return RepNum(sr[:(-gth)])

    def __repr__(self):
        return "{1}({0})".format(",".join(self._li),self.__class__.__name__)

    def __str__(self):
        li = []
        for y in self._li:
            name, val = y.split('=')
            value = int(val)
            if value == 1:
                name = name[:-1]
            li.append("{0} {1}".format(val,name))
        return "{0}".format(", ".join(li))
