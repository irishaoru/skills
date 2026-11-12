"""Review coverage and evidence regression tests; no network requests."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from openpyxl import load_workbook
import server


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'outputs').mkdir()
        self.sid = 'abcdef123456'
        self.rows = [dict(candidate_id=str(i), title='Product Intern',
                          listing_url='https://example.com/' + str(i),
                          description='Currently enrolled in a business degree.') for i in range(2)]
        (self.root / 'outputs' / f'internships-{self.sid}.json').write_text(
            json.dumps(dict(rows=self.rows, profile={}, errors=[])))
        self.patch = patch.object(server, '__file__', str(self.root / 'server.py'))
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def assessments(self):
        return [dict(candidate_id=row['candidate_id'], fit='possible',
                     fit_evidence=['Currently enrolled in a business degree.'],
                     fit_reason='Business study is relevant; other fit remains unknown.',
                     eligibility='uncertain', checks={
                         key: dict(status='unknown', reason='Needs confirmation.', evidence=[])
                         for key in ['education', 'skills', 'locations', 'availability', 'work_authorization']})
                for row in self.rows]

    def test_missing_duplicate_and_extra_candidates_rejected(self):
        items = self.assessments()
        for invalid in [items[:1], [items[0], items[0]], items + [dict(items[0], candidate_id='extra')]]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                server.finalize_internship_review(self.sid, invalid)

    def test_evidence_and_conclusions_validated(self):
        for kind in ['missing_dimension', 'fake_quote', 'unsupported_met', 'false_eligibility', 'unsupported_fit']:
            items = self.assessments()
            if kind == 'missing_dimension':
                del items[0]['checks']['skills']
            elif kind == 'fake_quote':
                items[0]['checks']['skills']['evidence'] = ['SQL required']
            elif kind == 'unsupported_met':
                items[0]['checks']['skills']['status'] = 'met'
            elif kind == 'false_eligibility':
                items[0]['eligibility'] = 'meets_stated_requirements'
            else:
                items[0]['fit_evidence'] = []
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                server.finalize_internship_review(self.sid, items)

    def test_all_rows_exported_with_unknowns_and_evidence(self):
        items = self.assessments()
        items[0]['checks']['education'] = dict(status='met', reason='Profile lists business degree.',
            evidence=['Currently enrolled in a business degree.'])
        real_export = server.export_results
        with patch.object(server, 'export_results', side_effect=lambda rows, profile, errors:
                          real_export(rows, profile, errors, output_dir=self.root / 'outputs')):
            result = server.finalize_internship_review(self.sid, items)
        self.assertEqual(result['review_coverage'], {'required': 2, 'completed': 2})
        workbook = load_workbook(result['xlsx_path'])
        self.addCleanup(workbook.close)
        sheet = workbook['Internships']
        self.assertEqual(sheet.max_row, 3)
        self.assertEqual(sheet['L2'].value, 'uncertain')
        self.assertIn('Currently enrolled', sheet['M2'].value)
        self.assertIn('Reviewed', sheet['J3'].value)


if __name__ == '__main__':
    unittest.main()
