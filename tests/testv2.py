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

import unittest
from NumRep import NumRep, HUNDREDS, THOUSANDS, CRORES, TENS, ONES, LAKHS

class Tester(unittest.TestCase):
    def setUp(self):
        self.numrep = NumRep(123456789111)

    def test_repr(self):
        self.assertEqual(repr(self.numrep),'NumRep(Crores=12345,Lakhs=67,Thousands=89,Hundreds=1,Tens=1,Ones=1)')

    def test_str(self):
        self.assertEqual(str(self.numrep),'12345 Crores, 67 Lakhs, 89 Thousands, 1 Hundred, 1 Ten, 1 One')

    def test_adds_int(self):
        calcd = self.numrep + 1111111111111
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111+1111111111111)))
        self.assertEqual(calcd.crores, 123456)
        self.assertEqual(calcd.lakhs, 79)
        self.assertEqual(calcd.thousands, 0)
        self.assertEqual(calcd.hundreds, 2)
        self.assertEqual(calcd.tens, 2)
        self.assertEqual(calcd.ones, 2)
        self.assertEqual(calcd.number, int((123456789111+1111111111111)))
        self.assertEqual(repr(calcd),'NumRep(Crores=123456,Lakhs=79,Hundreds=2,Tens=2,Ones=2)')
        self.assertEqual(str(calcd),'123456 Crores, 79 Lakhs, 2 Hundreds, 2 Tens, 2 Ones')

    def test_subtracts_int(self):
        calcd = self.numrep - 111111111111
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111-111111111111)))
        self.assertEqual(calcd.crores, 1234)
        self.assertEqual(calcd.lakhs, 56)
        self.assertEqual(calcd.thousands, 78)
        self.assertEqual(calcd.hundreds, 0)
        self.assertEqual(calcd.tens, 0)
        self.assertEqual(calcd.ones, 0)
        self.assertEqual(calcd.number, int((123456789111-111111111111)))
        self.assertEqual(repr(calcd),'NumRep(Crores=1234,Lakhs=56,Thousands=78)')
        self.assertEqual(str(calcd),'1234 Crores, 56 Lakhs, 78 Thousands')

    def test_multiplies_int(self):
        calcd = self.numrep * 2
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111*2)))
        self.assertEqual(calcd.crores, 24691)
        self.assertEqual(calcd.lakhs, 35)
        self.assertEqual(calcd.thousands, 78)
        self.assertEqual(calcd.hundreds, 2)
        self.assertEqual(calcd.tens, 2)
        self.assertEqual(calcd.ones, 2)
        self.assertEqual(calcd.number, int((123456789111*2)))
        self.assertEqual(repr(calcd),'NumRep(Crores=24691,Lakhs=35,Thousands=78,Hundreds=2,Tens=2,Ones=2)')
        self.assertEqual(str(calcd),'24691 Crores, 35 Lakhs, 78 Thousands, 2 Hundreds, 2 Tens, 2 Ones')

    def test_divs_int(self):
        calcd = self.numrep / 2
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111/2)))
        self.assertEqual(calcd.crores, 6172)
        self.assertEqual(calcd.lakhs, 83)
        self.assertEqual(calcd.thousands, 94)
        self.assertEqual(calcd.hundreds, 5)
        self.assertEqual(calcd.tens, 5)
        self.assertEqual(calcd.ones, 5)
        self.assertEqual(calcd.number, int((123456789111/2)))
        self.assertEqual(repr(calcd),'NumRep(Crores=6172,Lakhs=83,Thousands=94,Hundreds=5,Tens=5,Ones=5)')
        self.assertEqual(str(calcd),'6172 Crores, 83 Lakhs, 94 Thousands, 5 Hundreds, 5 Tens, 5 Ones')

    def test_mod_int(self):
        calcd = self.numrep % 22222222
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111%22222222)))
        self.assertEqual(calcd.crores, 1)
        self.assertEqual(calcd.lakhs, 23)
        self.assertEqual(calcd.thousands, 45)
        self.assertEqual(calcd.hundreds, 9)
        self.assertEqual(calcd.tens, 0)
        self.assertEqual(calcd.ones, 1)
        self.assertEqual(calcd.number, int((123456789111%22222222)))
        self.assertEqual(repr(calcd),'NumRep(Crores=1,Lakhs=23,Thousands=45,Hundreds=9,Ones=1)')
        self.assertEqual(str(calcd),'1 Crore, 23 Lakhs, 45 Thousands, 9 Hundreds, 1 One')

    def test_divmod_int(self):
        calcd, calc2d = divmod(self.numrep, 22222222)
        self.assertIsInstance(calcd, NumRep)
        self.assertIsInstance(calc2d, NumRep)
        self.assertEqual((calcd,calc2d), divmod(123456789111, 22222222))
        self.assertEqual(calcd.crores, 0)
        self.assertEqual(calcd.lakhs, 0)
        self.assertEqual(calcd.thousands, 5)
        self.assertEqual(calcd.hundreds, 5)
        self.assertEqual(calcd.tens, 5)
        self.assertEqual(calcd.ones, 5)
        self.assertEqual(calcd.number, int((123456789111//22222222)))
        self.assertEqual(repr(calcd),'NumRep(Thousands=5,Hundreds=5,Tens=5,Ones=5)')
        self.assertEqual(str(calcd),'5 Thousands, 5 Hundreds, 5 Tens, 5 Ones')
        self.assertEqual(calc2d.crores, 1)
        self.assertEqual(calc2d.lakhs, 23)
        self.assertEqual(calc2d.thousands, 45)
        self.assertEqual(calc2d.hundreds, 9)
        self.assertEqual(calc2d.tens, 0)
        self.assertEqual(calc2d.ones, 1)
        self.assertEqual(calc2d.number, int((123456789111%22222222)))
        self.assertEqual(repr(calc2d),'NumRep(Crores=1,Lakhs=23,Thousands=45,Hundreds=9,Ones=1)')
        self.assertEqual(str(calc2d),'1 Crore, 23 Lakhs, 45 Thousands, 9 Hundreds, 1 One')

    def test_adds_numrep(self):
        calcd = self.numrep + NumRep(1111111111111)
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111+1111111111111)))
        self.assertEqual(calcd.crores, 123456)
        self.assertEqual(calcd.lakhs, 79)
        self.assertEqual(calcd.thousands, 0)
        self.assertEqual(calcd.hundreds, 2)
        self.assertEqual(calcd.tens, 2)
        self.assertEqual(calcd.ones, 2)
        self.assertEqual(calcd.number, int((123456789111+1111111111111)))
        self.assertEqual(repr(calcd),'NumRep(Crores=123456,Lakhs=79,Hundreds=2,Tens=2,Ones=2)')
        self.assertEqual(str(calcd),'123456 Crores, 79 Lakhs, 2 Hundreds, 2 Tens, 2 Ones')

    def test_subtracts_numrep(self):
        calcd = self.numrep - NumRep(111111111111)
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111-111111111111)))
        self.assertEqual(calcd.crores, 1234)
        self.assertEqual(calcd.lakhs, 56)
        self.assertEqual(calcd.thousands, 78)
        self.assertEqual(calcd.hundreds, 0)
        self.assertEqual(calcd.tens, 0)
        self.assertEqual(calcd.ones, 0)
        self.assertEqual(calcd.number, int((123456789111-111111111111)))
        self.assertEqual(repr(calcd),'NumRep(Crores=1234,Lakhs=56,Thousands=78)')
        self.assertEqual(str(calcd),'1234 Crores, 56 Lakhs, 78 Thousands')

    def test_multiplies_numrep(self):
        calcd = self.numrep * NumRep(2)
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111*2)))
        self.assertEqual(calcd.crores, 24691)
        self.assertEqual(calcd.lakhs, 35)
        self.assertEqual(calcd.thousands, 78)
        self.assertEqual(calcd.hundreds, 2)
        self.assertEqual(calcd.tens, 2)
        self.assertEqual(calcd.ones, 2)
        self.assertEqual(calcd.number, int((123456789111*2)))
        self.assertEqual(repr(calcd),'NumRep(Crores=24691,Lakhs=35,Thousands=78,Hundreds=2,Tens=2,Ones=2)')
        self.assertEqual(str(calcd),'24691 Crores, 35 Lakhs, 78 Thousands, 2 Hundreds, 2 Tens, 2 Ones')

    def test_divs_numrep(self):
        calcd = self.numrep / NumRep(2)
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111/2)))
        self.assertEqual(calcd.crores, 6172)
        self.assertEqual(calcd.lakhs, 83)
        self.assertEqual(calcd.thousands, 94)
        self.assertEqual(calcd.hundreds, 5)
        self.assertEqual(calcd.tens, 5)
        self.assertEqual(calcd.ones, 5)
        self.assertEqual(calcd.number, int((123456789111/2)))
        self.assertEqual(repr(calcd),'NumRep(Crores=6172,Lakhs=83,Thousands=94,Hundreds=5,Tens=5,Ones=5)')
        self.assertEqual(str(calcd),'6172 Crores, 83 Lakhs, 94 Thousands, 5 Hundreds, 5 Tens, 5 Ones')

    def test_mod_numrep(self):
        calcd = self.numrep % NumRep(22222222)
        self.assertIsInstance(calcd, NumRep)
        self.assertEqual(calcd, int((123456789111%22222222)))
        self.assertEqual(calcd.crores, 1)
        self.assertEqual(calcd.lakhs, 23)
        self.assertEqual(calcd.thousands, 45)
        self.assertEqual(calcd.hundreds, 9)
        self.assertEqual(calcd.tens, 0)
        self.assertEqual(calcd.ones, 1)
        self.assertEqual(calcd.number, int((123456789111%22222222)))
        self.assertEqual(repr(calcd),'NumRep(Crores=1,Lakhs=23,Thousands=45,Hundreds=9,Ones=1)')
        self.assertEqual(str(calcd),'1 Crore, 23 Lakhs, 45 Thousands, 9 Hundreds, 1 One')

    def test_divmod_numrep(self):
        calcd, calc2d = divmod(self.numrep, NumRep(22222222))
        self.assertIsInstance(calcd, NumRep)
        self.assertIsInstance(calc2d, NumRep)
        self.assertEqual((calcd,calc2d), divmod(123456789111, 22222222))
        self.assertEqual(calcd.crores, 0)
        self.assertEqual(calcd.lakhs, 0)
        self.assertEqual(calcd.thousands, 5)
        self.assertEqual(calcd.hundreds, 5)
        self.assertEqual(calcd.tens, 5)
        self.assertEqual(calcd.ones, 5)
        self.assertEqual(calcd.number, int((123456789111//22222222)))
        self.assertEqual(repr(calcd),'NumRep(Thousands=5,Hundreds=5,Tens=5,Ones=5)')
        self.assertEqual(str(calcd),'5 Thousands, 5 Hundreds, 5 Tens, 5 Ones')
        self.assertEqual(calc2d.crores, 1)
        self.assertEqual(calc2d.lakhs, 23)
        self.assertEqual(calc2d.thousands, 45)
        self.assertEqual(calc2d.hundreds, 9)
        self.assertEqual(calc2d.tens, 0)
        self.assertEqual(calc2d.ones, 1)
        self.assertEqual(calc2d.number, int((123456789111%22222222)))
        self.assertEqual(repr(calc2d),'NumRep(Crores=1,Lakhs=23,Thousands=45,Hundreds=9,Ones=1)')
        self.assertEqual(str(calc2d),'1 Crore, 23 Lakhs, 45 Thousands, 9 Hundreds, 1 One')

    def test_bool(self):
        a = NumRep(0)
        self.assertFalse(a)
        a = NumRep(1)
        self.assertTrue(a)

    def test_abs(self):
        self.assertEqual(self.numrep, abs(123456789111))

    def test_lt_int(self):
        self.assertTrue(self.numrep < 123456789112)
        self.assertFalse(self.numrep < 123456789110)

    def test_gt_int(self):
        self.assertTrue(self.numrep > 123456789110)
        self.assertFalse(self.numrep > 123456789112)

    def test_ge_int(self):
        self.assertTrue(self.numrep >= 123456789110)
        self.assertFalse(self.numrep >= 123456789112)
        self.assertTrue(self.numrep >= 123456789111)

    def test_le_int(self):
        self.assertTrue(self.numrep <= 123456789112)
        self.assertFalse(self.numrep <= 123456789110)
        self.assertTrue(self.numrep <= 123456789111)

    def test_lt_numrep(self):
        self.assertTrue(self.numrep < NumRep(123456789112))
        self.assertFalse(self.numrep < NumRep(123456789110))

    def test_gt_numrep(self):
        self.assertTrue(self.numrep > NumRep(123456789110))
        self.assertFalse(self.numrep > NumRep(123456789112))

    def test_ge_numrep(self):
        self.assertTrue(self.numrep >= NumRep(123456789110))
        self.assertFalse(self.numrep >= NumRep(123456789112))
        self.assertTrue(self.numrep >= NumRep(123456789111))

    def test_le_numrep(self):
        self.assertTrue(self.numrep <= NumRep(123456789112))
        self.assertFalse(self.numrep <= NumRep(123456789110))
        self.assertTrue(self.numrep <= NumRep(123456789111))

    def test_all_func(self):
        self.assertEqual(self.numrep.all(CRORES),12345)
        self.assertEqual(self.numrep.all(LAKHS),1234567)
        self.assertEqual(self.numrep.all(THOUSANDS),123456789)
        self.assertEqual(self.numrep.all(HUNDREDS),1234567891)
        self.assertEqual(self.numrep.all(TENS),12345678911)
        self.assertEqual(self.numrep.all(ONES),123456789111)
        self.assertEqual(self.numrep.all('crores'),12345)
        self.assertEqual(self.numrep.all('lakhs'),1234567)
        self.assertEqual(self.numrep.all('thousands'),123456789)
        self.assertEqual(self.numrep.all('hundreds'),1234567891)
        self.assertEqual(self.numrep.all('tens'),12345678911)
        self.assertEqual(self.numrep.all('ones'),123456789111)

    def test_raises(self):
        with self.assertRaisesRegex(TypeError,'Not a valid Number'):
            NumRep('11a')
        with self.assertRaisesRegex(TypeError,'Not a valid denomination'):
            self.numrep.all('invalid')

if __name__ == '__main__':
    unittest.main()
