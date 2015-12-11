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

    You can do arithmetic operations on it too, eg:
        >>> a = NumRep(1234456789123)
        >>> a
        NumRep(Crores=123445,Lakhs=67,Thousands=89,Hundreds=1,Tens=2,Ones=3)
        >>> a + 1
        NumRep(Crores=123445,Lakhs=67,Thousands=89,Hundreds=1,Tens=2,Ones=4)

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

from .funcs import NumRep