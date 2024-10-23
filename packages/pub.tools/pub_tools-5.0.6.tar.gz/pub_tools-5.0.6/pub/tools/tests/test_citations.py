import unittest

from .. import entrez
from ..citations import book_citation
from ..citations import chapter_citation
from ..citations import conference_citation
from ..citations import journal_citation
from ..citations import monograph_citation
from ..citations import period
from ..citations import publication_citation
from ..citations import punctuate
from ..citations import report_citation
from ..schema import Abstract
from ..schema import BookRecord
from ..schema import ChapterRecord
from ..schema import ConferenceRecord
from ..schema import JournalRecord
from ..schema import MonographRecord
from ..schema import Person
from ..schema import ReportRecord


class TestCitations(unittest.TestCase):
    maxDiff = None

    def test_citation_basics(self):
        start = ''
        expected = ''
        self.assertEqual(punctuate(start, ''), expected)
        start = 'foo'
        expected = 'foo.'
        self.assertEqual(punctuate(start, '.'), expected)
        start = 'foo+'
        expected = 'foo+'
        self.assertEqual(punctuate(start, '+'), expected)
        start = 'foo'
        expected = 'foo. '
        self.assertEqual(period(start), expected)
        start = 'foo.'
        expected = 'foo. '
        self.assertEqual(period(start), expected)

    def test_journal_citation(self):
        record = JournalRecord(
            title='My title',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Carter', first_name='', initial='G')
            ],
            journal='Sample Journal',
            pubdate='Jan 2007',
            volume='4',
            issue='5',
            pagination='345-7',
            pubmodel='Print',
            abstract=[],
            pubstatus='print',
            medium='',
            pmid=''
        )
        citation = '<span class="citation">Wohnlich E, Carter G. My title. <i>Sample Journal</i> ' \
                   'Jan 2007;4(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, publication=record))

        record.issue = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. <i>Sample Journal</i> ' \
                   'Jan 2007;4:345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, publication=record))

        record.issue = '5'
        record.volume = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. <i>Sample Journal</i> ' \
                   'Jan 2007;(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, publication=record))

        record.pagination = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. <i>Sample Journal</i> ' \
                   'Jan 2007;(5).</span>'
        self.assertEqual(citation, journal_citation(html=True, publication=record))

        record.journal = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. Jan 2007;(5).</span>'
        self.assertEqual(citation, journal_citation(html=True, publication=record))

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
        record = JournalRecord(
            title='My title',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Carter', first_name='', initial='G')
            ],
            journal='Sample Journal',
            pubdate='Jan 2007',
            volume='4',
            issue='5',
            pagination='345-7',
            pubmodel='Print',
            abstract=[Abstract(label='INTRO', text='my findings', nlmcategory='')],
        )
        citation = '<span class="citation">Wohnlich E, Carter G. My title. <i>Sample ' \
                   'Journal</i> Jan 2007;4(5):345-7. <br/>' \
                   '<div class="citationAbstract"><p class="abstractHeader"><strong>Abstract</strong></p>' \
                   '<p>INTRO: my findings</p></div></span>'
        self.assertEqual(citation, journal_citation(html=True, use_abstract=True, publication=record))

    def test_book_citation(self):
        record = BookRecord(
            title='My title',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Carter', first_name='', initial='G'),
            ],
            editors=[
                Person(last_name='Van Halen', first_name='', initial='E'),
            ],
            edition='First Edition',
            pubdate='2007 Dec',
            publisher='Doubleday',
            pubplace='New York',
            pagination='243',
            series='My series',
        )
        citation = '<span class="citation">Wohnlich E, Carter G. My title. First Edition. ' \
                   'Van Halen E, editor. New York: ' \
                   'Doubleday; 2007 Dec. p. 243. (My series)</span>'
        self.assertEqual(citation, book_citation(html=True, publication=record))

        record.pubdate = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. First Edition. Van Halen E, ' \
                   'editor. New York: ' \
                   'Doubleday. p. 243. (My series)</span>'
        self.assertEqual(citation, book_citation(html=True, publication=record))

        record.publisher = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. First Edition. Van Halen E, ' \
                   'editor. New York. ' \
                   'p. 243. (My series)</span>'
        self.assertEqual(citation, book_citation(html=True, publication=record))

        record.authors = []
        citation = '<span class="citation">Van Halen E, editor. My title. First Edition. New York. p. 243. ' \
                   '(My series)</span>'
        self.assertEqual(citation, book_citation(html=True, publication=record))

    def test_chapter_citation(self):
        record = ChapterRecord(
            title='My title',
            booktitle='My Book',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Carter', first_name='', initial='G')
            ],
            editors=[
                Person(last_name='Van Halen', first_name='', initial='E')
            ],
            edition='First Edition',
            pubdate='2007 Dec',
            publisher='Doubleday',
            pubplace='New York',
            pagination='243',
            series='My series',
        )
        citation = '<span class="citation">Wohnlich E, Carter G. My title. In: Van Halen E, editor. ' \
                   'My Book. First Edition. ' \
                   'New York: Doubleday; 2007 Dec. p. 243. (My series)</span>'
        self.assertEqual(citation, chapter_citation(html=True, publication=record))

        record.pubdate = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. In: Van Halen E, editor. ' \
                   'My Book. First Edition. ' \
                   'New York: Doubleday. p. 243. (My series)</span>'
        self.assertEqual(citation, chapter_citation(html=True, publication=record))

        record.publisher = ''
        citation = '<span class="citation">Wohnlich E, Carter G. My title. In: Van Halen E, editor. ' \
                   'My Book. First Edition. ' \
                   'New York. p. 243. (My series)</span>'
        self.assertEqual(citation, chapter_citation(html=True, publication=record))

        record.authors = []
        citation = '<span class="citation">Van Halen E, editor. My title. In: My Book. First Edition. ' \
                   'New York. p. 243. ' \
                   '(My series)</span>'
        self.assertEqual(citation, chapter_citation(html=True, publication=record))

    def test_conference_citation(self):
        record = ConferenceRecord(
            title='My title',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Battle', first_name='', initial='J')
            ],
            editors=[
                Person(last_name='Sagan', first_name='', initial='C'),
                Person(last_name='Thorne', first_name='', initial='K')
            ],
            conferencename='Conference name',
            conferencedate='2007 Dec',
            place='New York',
            pubdate='2008 Jan',
            publisher='Doubleday',
            pubplace='Boston',
            pagination='345',
        )
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Sagan C, Thorne K, editors. ' \
                   '<i>Proceedings of Conference ' \
                   'name</i>; 2007 Dec; New York. Boston: Doubleday; 2008 Jan. p. 345.</span>'
        self.assertEqual(citation, conference_citation(html=True, publication=record))

        record.authors = []
        citation = '<span class="citation">Sagan C, Thorne K, editors. My title. <i>Proceedings of ' \
                   'Conference name</i>; 2007 Dec; New ' \
                   'York. Boston: Doubleday; 2008 Jan. p. 345.</span>'
        self.assertEqual(citation, conference_citation(html=True, publication=record))

        record.authors = [
            Person(
                last_name='Wohnlich',
                first_name='',
                initial='E',
            ),
            Person(
                last_name='Battle',
                first_name='',
                initial='J'
            )
        ]
        record.pagination = ''
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Sagan C, Thorne K, editors. ' \
                   '<i>Proceedings of Conference ' \
                   'name</i>; 2007 Dec; New York. Boston: Doubleday; 2008 Jan.</span>'
        self.assertEqual(citation, conference_citation(html=True, publication=record))

        record.publisher = ''
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Sagan C, Thorne K, editors. ' \
                   '<i>Proceedings of Conference ' \
                   'name</i>; 2007 Dec; New York. Boston: 2008 Jan.</span>'
        self.assertEqual(citation, conference_citation(html=True, publication=record))

        record.pubplace = ''
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Sagan C, Thorne K, editors. ' \
                   '<i>Proceedings of Conference ' \
                   'name</i>; 2007 Dec; New York. 2008 Jan.</span>'
        self.assertEqual(citation, conference_citation(html=True, publication=record))

    def test_monograph_citation(self):
        record = MonographRecord(
            title='My title',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Battle', first_name='', initial='J')
            ],
            serieseditors=['Hawking S', 'Wheeler J'],
            series='Series name',
            reportnum='5',
            weburl='http://plone.org',
            pubdate='2010 Feb',
            publisher='Doubleday',
            pubplace='Baltimore'
        )
        citation = '<span class="citation">Wohnlich E, Battle J; My title. Series name. Hawking S, ' \
                   'Wheeler J, editors. Baltimore: ' \
                   'Doubleday; 2010 Feb. 5. Available at http://plone.org.</span>'
        self.assertEqual(citation, monograph_citation(html=True, publication=record))

        record.weburl = ''
        citation = '<span class="citation">Wohnlich E, Battle J; My title. Series name. Hawking S, ' \
                   'Wheeler J, editors. Baltimore: ' \
                   'Doubleday; 2010 Feb. 5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, publication=record))

        record.authors = []
        citation = '<span class="citation">Hawking S, Wheeler J, editors. My title. Series name. ' \
                   'Baltimore: Doubleday; 2010 Feb. ' \
                   '5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, publication=record))

        record.authors = [
            Person(last_name='Wohnlich', first_name='', initial='E'),
            Person(last_name='Battle', first_name='', initial='J')
        ]
        record.title = ''
        citation = '<span class="citation">Wohnlich E, Battle J; Series name. Hawking S, Wheeler J, ' \
                   'editors. Baltimore: Doubleday; ' \
                   '2010 Feb. 5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, publication=record))

        record.pubplace = ''
        citation = '<span class="citation">Wohnlich E, Battle J; Series name. Hawking S, Wheeler J, ' \
                   'editors. Doubleday; ' \
                   '2010 Feb. 5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, publication=record))

        record.publisher = ''
        citation = '<span class="citation">Wohnlich E, Battle J; Series name. Hawking S, Wheeler J, ' \
                   'editors. 2010 Feb. 5.</span>'
        self.assertEqual(citation, monograph_citation(html=True, publication=record))

    def test_report_citation(self):
        record = ReportRecord(
            title='My title',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Battle', first_name='', initial='J')
            ],
            editors=[
                Person(last_name='Hawking', first_name='', initial='S'),
                Person(last_name='Wheeler', first_name='', initial='J')
            ],
            series='Series name',
            reportnum='5',
            weburl='http://plone.org',
            pubdate='2010 Feb',
            publisher='Doubleday',
            pubplace='Baltimore'
        )
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Series name. Hawking S, ' \
                   'Wheeler J, editors. Baltimore: ' \
                   'Doubleday; 2010 Feb. 5. Available at http://plone.org.</span>'
        self.assertEqual(citation, report_citation(html=True, publication=record))

        record.weburl = ''
        citation = '<span class="citation">Wohnlich E, Battle J. My title. Series name. Hawking S, ' \
                   'Wheeler J, editors. Baltimore: ' \
                   'Doubleday; 2010 Feb. 5.</span>'
        self.assertEqual(citation, report_citation(html=True, publication=record))

        record.authors = []
        citation = '<span class="citation">Hawking S, Wheeler J, editors. My title. Series name. ' \
                   'Baltimore: Doubleday; 2010 Feb. ' \
                   '5.</span>'
        self.assertEqual(citation, report_citation(html=True, publication=record))

        record.authors = [
            Person(last_name='Wohnlich', first_name='', initial='E'),
            Person(last_name='Battle', first_name='', initial='J')
        ]
        record.title = ''
        citation = '<span class="citation">Wohnlich E, Battle J. Series name. Hawking S, Wheeler J, ' \
                   'editors. Baltimore: Doubleday; ' \
                   '2010 Feb. 5.</span>'
        self.assertEqual(citation, report_citation(html=True, publication=record))

        record.pubplace = ''
        citation = '<span class="citation">Wohnlich E, Battle J. Series name. Hawking S, Wheeler J, ' \
                   'editors. Doubleday; 2010 ' \
                   'Feb. 5.</span>'
        self.assertEqual(citation, report_citation(html=True, publication=record))

        record.publisher = ''
        citation = '<span class="citation">Wohnlich E, Battle J. Series name. Hawking S, Wheeler J, ' \
                   'editors. 2010 Feb. 5.</span>'
        self.assertEqual(citation, report_citation(html=True, publication=record))

    def test_non_latin1(self):
        record = JournalRecord(
            title='My title',
            authors=[
                Person(
                    last_name='Wohnliché',
                    initial='E',
                    first_name=''
                ),
                Person(
                    last_name='Carter',
                    initial='G',
                    first_name=''
                )],
            journal='Sample Journal',
            pubdate='Jan 2007',
            volume='4',
            issue='5',
            pagination='345-7',
            pubmodel='Print',
        )
        citation = '<span class="citation">Wohnliché E, Carter G. My title. <i>Sample Journal</i> ' \
                   'Jan 2007;4(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, publication=record))

    def test_html_chapter(self):
        record = ChapterRecord(
            title='Chapter 19. Estimating the Natural History of Breast Cancer from Bivariate Data on Age and '
                  'Tumor Size at Diagnosis',
            authors=[
                Person(
                    last_name='Zorin', first_name='', initial='AV'
                ),
                Person(
                    last_name='Edler', first_name='', initial='L',
                ),
                Person(
                    last_name='Hanin', first_name='', initial='LG',
                ),
                Person(
                    last_name='Yakovlev', first_name='', initial='AY',
                )
            ],
            editors=[
                Person(last_name='Edler', initial='L', first_name=''),
                Person(last_name='Kitsos', initial='CP', first_name='')
            ],
            pubdate='2006 Mar 17',
            pagination='317-27',
            edition='',
            series='Wiley Series in Probability and Statistics',
            pubplace='New York',
            booktitle='Recent Advances in Quantitative Methods for Cancer and Human Health Risk Assessment',
            publisher='John Wiley & Sons, Ltd'
        )
        citation = '<span class="citation">Zorin AV, Edler L, Hanin LG, Yakovlev AY. Chapter 19. ' \
                   'Estimating the Natural History ' \
                   'of Breast Cancer from Bivariate Data on Age and Tumor Size at Diagnosis. In: Edler L, ' \
                   'Kitsos CP, editors. Recent Advances in Quantitative Methods for Cancer and Human Health Risk ' \
                   'Assessment. New York: John Wiley &amp; Sons, Ltd; 2006 Mar 17. p. 317-27. (Wiley Series in ' \
                   'Probability and Statistics)</span>'
        self.assertEqual(citation, chapter_citation(html=True, publication=record))

    def test_linked_journal_citation(self):
        record = JournalRecord(
            title='My title.',
            authors=[
                Person(
                    last_name='Wohnlich',
                    initial='E',
                    first_name=''
                ),
                Person(
                    last_name='Carter',
                    initial='G',
                    first_name=''
                ),
            ],
            journal='Sample Journal',
            pubdate='Jan 2007',
            volume='4',
            issue='5',
            pagination='345-7',
            pubmodel='Print',
            abstract=[Abstract(label='INTRO', text='my findings', nlmcategory='')],
            pmid='12345678',
        )
        citation = '<span class="citation">Wohnlich E, Carter G. <a class="citation-pubmed-link" ' \
                   'href="https://pubmed.ncbi.nlm.nih.gov' \
                   '/12345678/">My title.</a> <i>Sample Journal</i> Jan 2007;4(5):345-7. <br/>' \
                   '<div class="citationAbstract"><p class="abstractHeader"><strong>Abstract</strong></p><p>INTRO: ' \
                   'my findings</p></div></span>'
        self.assertEqual(citation, journal_citation(html=True, link=True, use_abstract=True, publication=record))

    def test_citation_from_journal_dataclass(self):
        cit = publication_citation(publication=entrez.get_publication(pmid=12345678), html=True)
        self.assertEqual(cit, '<span class="citation">Ministerial Meeting on Population of '
                              'the Non-Aligned Movement (1993: '
                              'Bali). Denpasar Declaration on Population and Development. <i>Integration</i> 1994 '
                              'Jun;(40):27-9.</span>')

    def test_citation_from_chapter_dataclass(self):
        cit = publication_citation(publication=entrez.get_publication(pmid=22593940), html=True)
        self.assertEqual(cit, '<span class="citation">Kaefer CM, Milner JA, Benzie IFF, '
                              'Wachtel-Galor S. Herbs and Spices in '
                              'Cancer Prevention and Treatment. In: Herbal Medicine: Biomolecular and Clinical '
                              'Aspects. 2nd. Boca Raton (FL): CRC Press/Taylor &amp; Francis; 2011.</span>')

    def test_citation_from_book_dataclass(self):
        cit = publication_citation(publication=entrez.get_publication(pmid=12345678), html=True)
        self.assertEqual(cit, '<span class="citation">Ministerial Meeting on Population of the Non-Aligned '
                              'Movement (1993: '
                              'Bali). Denpasar Declaration on Population and Development. <i>Integration</i> 1994 '
                              'Jun;(40):27-9.</span>')

    def test_citation_html_title(self):
        record = JournalRecord(
            title='My &lt;title&gt;',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Carter', first_name='', initial='G')
            ],
            journal='Sample Journal',
            pubdate='Jan 2007',
            volume='4',
            issue='5',
            pagination='345-7',
            pubmodel='Print',
            abstract=[],
            pubstatus='print',
            medium='',
            pmid=''
        )
        citation = '<span class="citation">Wohnlich E, Carter G. My &lt;title&gt;. <i>Sample Journal</i> ' \
                   'Jan 2007;4(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, publication=record))

    def test_unescapted_journal_title(self):
        record = JournalRecord(
            title='My & title',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Carter', first_name='', initial='G')
            ],
            journal='Sample Journal',
            pubdate='Jan 2007',
            volume='4',
            issue='5',
            pagination='345-7',
            pubmodel='Print',
            abstract=[],
            pubstatus='print',
            medium='',
            pmid=''
        )
        citation = '<span class="citation">Wohnlich E, Carter G. My &amp; title. <i>Sample Journal</i> ' \
                   'Jan 2007;4(5):345-7.</span>'
        self.assertEqual(citation, journal_citation(html=True, publication=record))

    def test_bad_format_title(self):
        record = JournalRecord(
            title='My & &lt;title&gt;',
            authors=[
                Person(last_name='Wohnlich', first_name='', initial='E'),
                Person(last_name='Carter', first_name='', initial='G')
            ],
            journal='Sample Journal',
            pubdate='Jan 2007',
            volume='4',
            issue='5',
            pagination='345-7',
            pubmodel='Print',
            abstract=[],
            pubstatus='print',
            medium='',
            pmid=''
        )
        citation = ('<span class="citation">Wohnlich E, Carter G. My &amp; &lt;title&gt;. <i>Sample '
                    'Journal</i> Jan 2007;4(5):345-7.'
                    '</span>')
        self.assertEqual(citation, journal_citation(html=True, publication=record))
