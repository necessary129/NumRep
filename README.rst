NumRep
------

.. image:: https://travis-ci.org/necessary129/NumRep.svg
    :target: https://travis-ci.org/necessary129/NumRep

Version: 0.1

This module provides a way to represent the place values in a given number, eg:
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

This raises TypeError when you give it an invalid number, eg:
    >>> a = NumRep('notanumber1111')
    Traceback (most recent call last):
    ...
    TypeError: Not a valid Number.

And Every integer in the NumRep has a GetRep() method, which returns the Representation of the number itself, eg:
    >>> a = NumRep(123456789)
    >>> a
    NumRep(Crores=12,Lakhs=34,Thousands=56,Hundreds=7,Tens=8,Ones=9)
    >>> a.crores
    12
    >>> a.crores.GetRep()
    NumRep(Tens=1,Ones=2)
    >>> a.crores.GetRep().tens.GetRep()
    NumRep(Ones=1)

You can also do arithmetic operations on them and then use GetRep(), eg:
    >>> a = NumRep(123456789)
    >>> a
    NumRep(Crores=12,Lakhs=34,Thousands=56,Hundreds=7,Tens=8,Ones=9)
    >>> (a.crores - 2).GetRep()
    NumRep(Tens=1)

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


This class also provides an all() function, which gives you the real value of the given denomination, eg:
    >>> a = NumRep(1234456789123)
    >>> a.all('hundreds')
    12344567891
You can also use the values specified in the module for all(), eg:
    >>> a = NumRep(1234456789123)
    >>> a.all(CRORES)
    123445