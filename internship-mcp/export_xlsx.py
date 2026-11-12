"""Portable XLSX export for internship searches."""

from pathlib import Path
from uuid import uuid4

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


def text_cell(sheet, row, column, value):
    # Listings are untrusted text: never interpret a leading '=' as a formula.
    value = str(value)
    value = ''.join(c for c in value if ord(c) >= 32 or c in '\n\t\r')
    cell = sheet.cell(row, column, value[:32767])
    cell.data_type = 's'
    return cell


def export_results(rows, profile, errors, output_dir=None):
    directory = Path(output_dir) if output_dir else Path(__file__).parent / 'outputs'
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f'internships-{uuid4().hex[:12]}.xlsx'
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Internships'
    columns = [
        ('Role', 'title', 38), ('Company board', 'company_board', 22),
        ('Location', 'location', 30), ('Pay — listing evidence', 'pay_evidence', 65),
        ('Duration — listing evidence', 'duration_evidence', 65),
        ('Qualifications — listing evidence', 'qualification_evidence', 65),
        ('Application link', 'listing_url', 50), ('Last updated', 'updated_at', 26),
        ('Source', 'source', 18),
        ('Review status', 'review_status', 30),
        ('Fit assessment', 'fit_assessment', 65),
        ('Eligibility assessment', 'eligibility_assessment', 30),
        ('Eligibility checks and evidence', 'review_checks', 100),
        ('Fit evidence', 'fit_evidence', 65),
    ]
    for col, (label, key, width) in enumerate(columns, 1):
        cell = text_cell(sheet, 1, col, label)
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = PatternFill('solid', fgColor='16324F')
        sheet.column_dimensions[get_column_letter(col)].width = width
        for row_num, result in enumerate(rows, 2):
            value = result.get(key, 'Not specified')
            cell = text_cell(sheet, row_num, col, '\n'.join(value) if isinstance(value, list) else value)
            cell.alignment = Alignment(vertical='top', wrap_text=True)
            if key == 'listing_url' and str(value).startswith(('https://', 'http://')):
                cell.hyperlink = value
                cell.style = 'Hyperlink'
            if row_num % 2 == 0:
                cell.fill = PatternFill('solid', fgColor='EEF3F8')
    sheet.freeze_panes = 'C2'
    sheet.auto_filter.ref = f'A1:N{max(1, len(rows) + 1)}'
    sheet.row_dimensions[1].height = 32
    for row_num in range(2, len(rows) + 2):
        sheet.row_dimensions[row_num].height = 120
    notes = workbook.create_sheet('Search context')
    context = [
        ('About', 'Internship candidates, not verified eligibility matches.'),
        ('Pay and duration', 'Source excerpts may be incomplete or include unrelated mentions. Not specified means missing evidence, not unpaid or ineligible. Verify the linked listing.'),
        ('Company', 'Company board is a Greenhouse identifier, not a verified display name.'),
        ('Dates', 'Last updated is not the original posting date.'),
        ('Results', str(len(rows)) + ' rows. Zero rows can mean no matches; inspect board errors below.'),
        *[(key, value) for key, value in profile.items()],
        *[('Board error: ' + error['board'], error['error']) for error in errors],
    ]
    notes.column_dimensions['A'].width = 25
    notes.column_dimensions['B'].width = 100
    for row_num, (key, value) in enumerate(context, 1):
        text_cell(notes, row_num, 1, key).font = Font(bold=True)
        text_cell(notes, row_num, 2, value).alignment = Alignment(wrap_text=True, vertical='top')
        notes.row_dimensions[row_num].height = 45
    workbook.save(path)
    return str(path.resolve())
