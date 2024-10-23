import unittest

from ..citations import book_citation
from ..citations import chapter_citation
from ..citations import conference_citation
from ..citations import journal_citation
from ..citations import monograph_citation
from ..citations import report_citation


class TestCitationsBackwardsCompatibility(unittest.TestCase):
    """ This tests that the old method of using dicts is still valid. See test_citations for dataclass replacement """
    maxDiff = None

    def test_journal_citation(self):
        record = {
            'title': 'My title',
            'authors': [{'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Carter', 'iname': 'G'}],
            'journal': 'Sample Journal',
            'pubdate': 'Jan 2007',
            'volume': '4',
            'issue': '5',
            'pagination': '345-7',
            'pubmodel': 'Print',
            'italicize': True,
        }
        citation = '<span class="citation">Wohnlich E, Carter G. My title. ' \
                   '<i>Sample Journal</i> Jan 2007;4(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, **record))

        record['issue'] = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. ' \
                   '<i>Sample Journal</i> Jan 2007;4:345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, **record))

        record['issue'] = '5'
        record['volume'] = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. ' \
                   '<i>Sample Journal</i> Jan 2007;(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, **record))

        record['pagination'] = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. <i>Sample Journal</i> Jan 2007;(5).</span>'
        self.assertEqual(citation, journal_citation(html=True, **record))

        record['journal'] = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. Jan 2007;(5).</span>'
        self.assertEqual(citation, journal_citation(html=True, **record))

    def test_journal_link_citation(self):
        record = {
            'title': 'My title',
            'authors': [{'lname': 'Wohnlich', 'iname': 'E', 'fname': 'Eric'},
                        {'lname': 'Carter', 'iname': 'G', 'fname': 'Ginger'}],
            'journal': 'Sample Journal',
            'pubdate': 'Jan 2007',
            'volume': '4',
            'issue': '5',
            'pagination': '345-7',
            'pubmodel': 'Print',
            'pmid': '12345678',
            'italicize': True,
        }
        citation = '<span class="citation">Wohnlich E, Carter G. <a class="citation-pubmed-link" ' \
                   'href="https://pubmed.ncbi.nlm.nih.gov/12345678/">My title</a>. ' \
                   '<i>Sample Journal</i> Jan 2007;4(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, link=True, **record))

    def test_journal_abstract_citation(self):
        record = {
            'title': 'My title',
            'authors': [{'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Carter', 'iname': 'G'}],
            'journal': 'Sample Journal',
            'pubdate': 'Jan 2007',
            'volume': '4',
            'issue': '5',
            'pagination': '345-7',
            'pubmodel': 'Print',
            'abstract': [{'label': 'INTRO', 'text': 'my findings'}],
            'use_abstract': True
        }
        citation = '<span class="citation">Wohnlich E, Carter G. My title. ' \
                   '<i>Sample Journal</i> Jan 2007;4(5):345-7. <br/>' \
                   '<div class="citationAbstract"><p class="abstractHeader"><strong>Abstract</strong></p>' \
                   '<p>INTRO: my findings</p></div></span>'
        self.assertEqual(citation, journal_citation(html=True, **record))

    def test_book_citation(self):
        record = {
            'title': 'My title',
            'authors': ({'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Carter', 'iname': 'G'},),
            'editors': ({'lname': 'Van Halen', 'iname': 'E'},),
            'edition': 'First Edition',
            'pubdate': '2007 Dec',
            'publisher': 'Doubleday',
            'pubplace': 'New York',
            'pagination': '243',
            'series': 'My series',
        }
        citation = '<span class="citation">Wohnlich E, Carter G. My title. ' \
                   'First Edition. Van Halen E, editor. New York: ' \
                   'Doubleday; 2007 Dec. p. 243. (My series)</span>'
        self.assertEqual(citation, book_citation(html=True, **record))

        record['pubdate'] = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. ' \
                   'First Edition. Van Halen E, editor. New York: ' \
                   'Doubleday. p. 243. (My series)</span>'
        self.assertEqual(citation, book_citation(html=True, **record))

        record['publisher'] = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. ' \
                   'First Edition. Van Halen E, editor. New York. ' \
                   'p. 243. (My series)</span>'
        self.assertEqual(citation, book_citation(html=True, **record))

        record['authors'] = []
        citation = '<span class="citation">Van Halen E, editor. My title. ' \
                   'First Edition. New York. p. 243. (My series)</span>'
        self.assertEqual(citation, book_citation(html=True, **record))

    def test_chapter_citation(self):
        record = {
            'title': 'My title',
            'booktitle': 'My Book',
            'authors': ({'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Carter', 'iname': 'G'},),
            'editors': ({'lname': 'Van Halen', 'iname': 'E'},),
            'edition': 'First Edition',
            'pubdate': '2007 Dec',
            'publisher': 'Doubleday',
            'pubplace': 'New York',
            'pagination': '243',
            'series': 'My series',
        }
        citation = '<span class="citation">Wohnlich E, Carter G. My title. In: ' \
                   'Van Halen E, editor. My Book. First Edition. ' \
                   'New York: Doubleday; 2007 Dec. p. 243. (My series)</span>'
        self.assertEqual(citation, chapter_citation(html=True, **record))

        record['pubdate'] = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. In: ' \
                   'Van Halen E, editor. My Book. First Edition. ' \
                   'New York: Doubleday. p. 243. (My series)</span>'
        self.assertEqual(citation, chapter_citation(html=True, **record))

        record['publisher'] = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. In: ' \
                   'Van Halen E, editor. My Book. First Edition. ' \
                   'New York. p. 243. (My series)</span>'
        self.assertEqual(citation, chapter_citation(html=True, **record))

        record['authors'] = []
        citation = '<span class="citation">Van Halen E, editor. My title. ' \
                   'In: My Book. First Edition. New York. p. 243. ' \
                   '(My series)</span>'
        self.assertEqual(citation, chapter_citation(html=True, **record))

    def test_conference_citation(self):
        record = {
            'title': 'My title',
            'booktitle': 'My Book',
            'authors': ({'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Battle', 'iname': 'J'},),
            'editors': ({'lname': 'Sagan', 'iname': 'C'}, {'lname': 'Thorne', 'iname': 'K'}),
            'conferencename': 'Conference name',
            'conferencedate': '2007 Dec',
            'place': 'New York',
            'pubdate': '2008 Jan',
            'publisher': 'Doubleday',
            'pubplace': 'Boston',
            'pagination': '345',
            'italicize': True,
        }
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Sagan C, ' \
                   'Thorne K, editors. <i>Proceedings of Conference ' \
                   'name</i>; 2007 Dec; New York. Boston: Doubleday; 2008 Jan. p. 345.</span>'
        self.assertEqual(citation, conference_citation(html=True, **record))

        record['authors'] = []
        citation = '<span class="citation">Sagan C, Thorne K, editors. My title. ' \
                   '<i>Proceedings of Conference name</i>; 2007 Dec; New ' \
                   'York. Boston: Doubleday; 2008 Jan. p. 345.</span>'
        self.assertEqual(citation, conference_citation(html=True, **record))

        record['authors'] = ({'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Battle', 'iname': 'J'},)
        record['pagination'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Sagan C, Thorne K, editors. ' \
                   '<i>Proceedings of Conference ' \
                   'name</i>; 2007 Dec; New York. Boston: Doubleday; 2008 Jan.</span>'
        self.assertEqual(citation, conference_citation(html=True, **record))

        record['publisher'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Sagan C, Thorne K, editors. ' \
                   '<i>Proceedings of Conference ' \
                   'name</i>; 2007 Dec; New York. Boston: 2008 Jan.</span>'
        self.assertEqual(citation, conference_citation(html=True, **record))

        record['pubplace'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Sagan C, Thorne K, editors. ' \
                   '<i>Proceedings of Conference ' \
                   'name</i>; 2007 Dec; New York. 2008 Jan.</span>'
        self.assertEqual(citation, conference_citation(html=True, **record))

    def test_monograph_citation(self):
        record = {'title': 'My title',
                  'booktitle': 'My Book',
                  'authors': [{'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Battle', 'iname': 'J'}],
                  'serieseditors': ('Hawking S', 'Wheeler J'),
                  'series': 'Series name',
                  'reportnum': '5',
                  'weburl': 'http://plone.org',
                  'pubdate': '2010 Feb',
                  'publisher': 'Doubleday',
                  'pubplace': 'Baltimore', }
        citation = '<span class="citation">Wohnlich E, Battle J; My title. Series name. Hawking S, ' \
                   'Wheeler J, editors. Baltimore: ' \
                   'Doubleday; 2010 Feb. 5. Available at http://plone.org.</span>'
        self.assertEqual(citation, monograph_citation(html=True, **record))

        record['weburl'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J; My title. Series name. Hawking S, ' \
                   'Wheeler J, editors. Baltimore: ' \
                   'Doubleday; 2010 Feb. 5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, **record))

        record['authors'] = []
        citation = '<span class="citation">Hawking S, Wheeler J, editors. My title. Series name. ' \
                   'Baltimore: Doubleday; 2010 Feb. ' \
                   '5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, **record))

        record['authors'] = ({'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Battle', 'iname': 'J'},)
        record['title'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J; Series name. Hawking S, Wheeler J, ' \
                   'editors. Baltimore: Doubleday; ' \
                   '2010 Feb. 5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, **record))

        record['pubplace'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J; Series name. Hawking S, ' \
                   'Wheeler J, editors. Doubleday; ' \
                   '2010 Feb. 5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, **record))

        record['publisher'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J; Series name. Hawking S, Wheeler J, ' \
                   'editors. 2010 Feb. 5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, **record))

    def test_report_citation(self):
        record = {'title': 'My title',
                  'booktitle': 'My Book',
                  'authors': ({'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Battle', 'iname': 'J'},),
                  'editors': ({'lname': 'Hawking', 'iname': 'S'}, {'lname': 'Wheeler', 'iname': 'J'},),
                  'series': 'Series name',
                  'reportnum': '5',
                  'weburl': 'http://plone.org',
                  'pubdate': '2010 Feb',
                  'publisher': 'Doubleday',
                  'pubplace': 'Baltimore', }
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Series name. Hawking S, ' \
                   'Wheeler J, editors. Baltimore: ' \
                   'Doubleday; 2010 Feb. 5. Available at http://plone.org.</span>'
        self.assertEqual(citation, report_citation(html=True, **record))

        record['weburl'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Series name. Hawking S, ' \
                   'Wheeler J, editors. Baltimore: ' \
                   'Doubleday; 2010 Feb. 5.</span>'
        self.assertEqual(citation, report_citation(html=True, **record))

        record['authors'] = []
        citation = '<span class="citation">Hawking S, Wheeler J, editors. My title. Series name. ' \
                   'Baltimore: Doubleday; 2010 Feb. ' \
                   '5.</span>'
        self.assertEqual(citation, report_citation(html=True, **record))

        record['authors'] = ({'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Battle', 'iname': 'J'},)
        record['title'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J. Series name. Hawking S, Wheeler J, ' \
                   'editors. Baltimore: Doubleday; ' \
                   '2010 Feb. 5.</span>'
        self.assertEqual(citation, report_citation(html=True, **record))

        record['pubplace'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J. Series name. Hawking S, Wheeler J, ' \
                   'editors. Doubleday; 2010 ' \
                   'Feb. 5.</span>'
        self.assertEqual(citation, report_citation(html=True, **record))

        record['publisher'] = ''
        citation = '<span class="citation">Wohnlich E, Battle J. Series name. Hawking S, Wheeler J, ' \
                   'editors. 2010 Feb. 5.</span>'
        self.assertEqual(citation, report_citation(html=True, **record))

    def test_non_latin1(self):
        record = {
            'title': 'My title',
            'authors': [{'lname': 'Wohnliché', 'iname': 'E'}, {'lname': 'Carter', 'iname': 'G'}],
            'journal': 'Sample Journal',
            'pubdate': 'Jan 2007',
            'volume': '4',
            'issue': '5',
            'pagination': '345-7',
            'pubmodel': 'Print',
            'italicize': True,
        }
        citation = '<span class="citation">Wohnliché E, Carter G. My title. <i>Sample Journal</i> Jan ' \
                   '2007;4(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, **record))

    def test_html_chapter(self):
        record = {
            'title': 'Chapter 19. Estimating the Natural History of Breast Cancer from Bivariate Data on Age and '
                     'Tumor Size at Diagnosis',
            'authors': [
                {'lname': 'Zorin', 'iname': 'AV'},
                {'lname': 'Edler', 'iname': 'L'},
                {'lname': 'Hanin', 'iname': 'LG'},
                {'lname': 'Yakovlev', 'iname': 'AY'}
            ],
            'editors': [{'lname': 'Edler', 'iname': 'L'}, {'lname': 'Kitsos', 'iname': 'CP'}],
            'pubdate': '2006 Mar 17',
            'pagination': '317-27',
            'edition': '',
            'series': 'Wiley Series in Probability and Statistics',
            'pubplace': 'New York',
            'booktitle': 'Recent Advances in Quantitative Methods for Cancer and Human Health Risk Assessment',
            'publisher': 'John Wiley & Sons, Ltd'
        }
        citation = '<span class="citation">Zorin AV, Edler L, Hanin LG, Yakovlev AY. Chapter 19. ' \
                   'Estimating the Natural History ' \
                   'of Breast Cancer from Bivariate Data on Age and Tumor Size at Diagnosis. In: Edler L, ' \
                   'Kitsos CP, editors. Recent Advances in Quantitative Methods for Cancer and Human Health Risk ' \
                   'Assessment. New York: John Wiley &amp; Sons, Ltd; 2006 Mar 17. p. 317-27. (Wiley Series in ' \
                   'Probability and Statistics)</span>'
        self.assertEqual(citation, chapter_citation(html=True, **record))

    def test_linked_journal_citation(self):
        record = {
            'title': 'My title.',
            'authors': [{'lname': 'Wohnlich', 'iname': 'E'}, {'lname': 'Carter', 'iname': 'G'}],
            'journal': 'Sample Journal',
            'pubdate': 'Jan 2007',
            'volume': '4',
            'issue': '5',
            'pagination': '345-7',
            'pubmodel': 'Print',
            'abstract': [{'label': 'INTRO', 'text': 'my findings'}],
            'use_abstract': True,
            'pmid': '12345678',
        }
        citation = '<span class="citation">Wohnlich E, Carter G. <a class="citation-pubmed-link" ' \
                   'href="https://pubmed.ncbi.nlm.nih.gov' \
                   '/12345678/">My title.</a> <i>Sample Journal</i> Jan 2007;4(5):345-7. <br/>' \
                   '<div class="citationAbstract"><p class="abstractHeader"><strong>Abstract</strong></p><p>INTRO: ' \
                   'my findings</p></div></span>'
        self.assertEqual(citation, journal_citation(html=True, link=True, **record))
