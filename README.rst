NumRep
------

.. image:: https://travis-ci.org/necessary129/NumRep.svg
    :target: https://travis-ci.org/necessary129/NumRep

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

This raises TypeError when you give a non-number to it., eg:
    >>> a = NumRep('notanumber123')
    Traceback (most recent call last):
    ...
    TypeError: Not a valid number

This class also provides an all() function, which gives you the real value of the given denomination, eg:
    >>> a = NumRep(1234456789123)
    >>> a.all('hundreds')
    12344567891