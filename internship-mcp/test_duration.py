"""Regression checks for duration evidence; run with python -m unittest discover."""

import unittest

from server import duration_evidence


class DurationEvidenceTests(unittest.TestCase):
    def test_reported_application_limit(self):
        # Exact E2 text from the first demonstration workbook.
        text = ('This is a 12-week internship during summer 2027.\n'
                'Hourly Rate: $40 — $40 USD Application Limit: Candidates may '
                'submit a maximum of 3 applications within a 6-month period.')
        self.assertEqual(duration_evidence(text),
                         ['This is a 12-week internship during summer 2027.'])

    def test_unrelated_time_is_not_duration(self):
        for text in ['Candidates may submit three applications within six months.',
                     'We offer 16 weeks of paid parental leave.',
                     'Internship applicants must graduate in summer 2028.',
                     'Internship requires 6 months of experience.',
                     'Join our team this summer.']:
            with self.subTest(text=text):
                self.assertEqual(duration_evidence(text), ['Not specified'])

    def test_html_blocks_and_encoded_html(self):
        self.assertEqual(duration_evidence(
            '&lt;p&gt;This is a 12-week paid summer internship.&lt;/p&gt;'
            '&lt;p&gt;Benefits include 6 months of parental leave.&lt;/p&gt;'),
            ['This is a 12-week paid summer internship.'])

    def test_duration_variants(self):
        for text in ['The internship lasts 12 weeks.',
                     'This is a 3-month internship.',
                     'A 10–12 week internship in New York.',
                     'Internship start date: May 17, 2027.',
                     'The internship runs during summer 2027.']:
            with self.subTest(text=text):
                self.assertEqual(duration_evidence(text), [text])


if __name__ == '__main__':
    unittest.main()
