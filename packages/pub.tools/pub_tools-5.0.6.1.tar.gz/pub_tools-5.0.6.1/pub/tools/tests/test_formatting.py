import unittest
from datetime import datetime

from .. import formatting
from ..config import NO_VALUE


class TestFormatting(unittest.TestCase):

    def test_blankify(self):
        preb = ''
        expected = NO_VALUE
        b = formatting.blankify(preb)
        self.assertEqual(b, expected)

    def test_date_slash(self):
        pre = '2010 July/August'
        expected = datetime(2010, 7, 1)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d, expected)

    def test_date_slash_str(self):
        pre = '2010 July/August'
        expected = '2010 Jul-Aug'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_slash_m_first(self):
        pre = 'July - August 1968'
        expected = '1968 Jul-Aug'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str1(self):
        pre = '8/11/2009'
        expected = '2009 Aug 11'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str2(self):
        pre = '8-11-2009'
        expected = '2009 Aug 11'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str3(self):
        pre = '15/8/2009'
        expected = '2009 Aug 15'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str4(self):
        pre = '2009 Aug 15'
        expected = '2009 Aug 15'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str5(self):
        pre = 'Aug 15 2009'
        expected = '2009 Aug 15'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str6(self):
        pre = '15 Aug 2009'
        expected = '2009 Aug 15'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str7(self):
        pre = '11 Aug 2009'
        expected = '2009 Aug 11'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str8(self):
        pre = 'Aug 15, 2009'
        expected = '2009 Aug 15'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str9(self):
        pre = 'Winter 2008'
        expected = '2008 Winter'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str10(self):
        pre = 'Fall-Winter 2008'
        expected = '2008 Fall-Winter'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str11(self):
        pre = '2009 Dec-2010 Jan'
        expected = '2009 Dec'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str12(self):
        pre = 'Dec 4 2009'
        expected = '2009 Dec 4'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_date_str13(self):
        pre = '2009 Aug 15th'
        expected = '2009 Aug 15'
        d = formatting.format_date_str(pre)
        self.assertEqual(d, expected)

    def test_datetime1(self):
        pre = '8/11/2009'
        expected = datetime(2009, 11, 8)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime2(self):
        pre = '8 11 2009'
        expected = datetime(2009, 11, 8)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime3(self):
        pre = '15/8/2009'
        expected = datetime(2009, 8, 15)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime4(self):
        pre = '15 Aug 2009'
        expected = datetime(2009, 8, 15)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime5(self):
        pre = '11 Aug 2009'
        expected = datetime(2009, 8, 11)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime6(self):
        pre = '15 Aug, 2009'
        expected = datetime(2009, 8, 15)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime7(self):
        pre = 'Winter 2008'
        expected = datetime(2008, 1, 1)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime8(self):
        pre = 'Jun 2008'
        expected = datetime(2008, 6, 1)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime9(self):
        pre = 'Spring-Fall 2008'
        expected = datetime(2008, 4, 1)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_datetime10(self):
        pre = '2009 Dec-2010 Jan'
        expected = datetime(2009, 12, 1)
        d = formatting.format_date(None, None, None, pre)
        self.assertEqual(d.year, expected.year)
        self.assertEqual(d.month, expected.month)
        self.assertEqual(d.day, expected.day)

    def test_date_ris1(self):
        pre = '2009 Jun 5'
        expected = '2009/06/05/'
        d = formatting.format_date_ris(pre)
        self.assertEqual(d, expected)

    def test_date_ris2(self):
        pre = '2009 Spring'
        expected = '2009///Spring'
        d = formatting.format_date_ris(pre)
        self.assertEqual(d, expected)

    def test_date_ris3(self):
        pre = '18 Apr 1978'
        expected = '1978/04/18/'
        d = formatting.format_date_ris(pre)
        self.assertEqual(d, expected)

    def test_date_ris4(self):
        # garbage/unknown. What does that 18 mean?
        pre = '18 1980'
        expected = '1980///18'
        d = formatting.format_date_ris(pre)
        self.assertEqual(d, expected)

    def test_date_ris5(self):
        pre = '1995 Aug 9-16'
        expected = '1995/08/9/'
        d = formatting.format_date_ris(pre)
        self.assertEqual(d, expected)

    def test_cook_date_end(self):
        pre = '2010 July/August'
        expected = datetime(2010, 8, 1)
        d = formatting.format_date(None, None, None, pre, end=True)
        self.assertEqual(d, expected)

    def test_date_months(self):
        pre = '2010 July-2011 August'
        expected = ['Jul 2010', 'Aug 2010', 'Sep 2010', 'Oct 2010', 'Nov 2010', 'Dec 2010', 'Jan 2011', 'Feb 2011',
                    'Mar 2011', 'Apr 2011', 'May 2011', 'Jun 2011', 'Jul 2011', 'Aug 2011']
        d = formatting.format_date_months(start=formatting.format_date(None, None, None, pre),
                                          end=formatting.format_date(None, None, None, pre, end=True))
        self.assertEqual(d, expected)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
