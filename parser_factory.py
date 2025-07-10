import os
import magic

from parsers.pdf_parser import PDFParser
from parsers.docx_parser import DOCXParser
from parsers.image_parser import ImageParser
from parsers.xlsx_parser import XLSXParser
from parsers.csv_parser import CSVParser

def get_parser(file_path):
    mime = magic.from_file(file_path, mime=True)
    ext = os.path.splitext(file_path)[1].lower()

    if mime == 'application/pdf' or ext == '.pdf':
        return PDFParser()
    elif mime in ['application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/msword'] or ext == '.docx':
        return DOCXParser()
    elif mime.startswith('image/') or ext in ['.jpg', '.jpeg', '.png']:
        return ImageParser()
    elif mime == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or ext == '.xlsx':
        return XLSXParser()
    elif mime == 'text/csv' or ext == '.csv':
        return CSVParser()
    else:
        raise ValueError(f"Unsupported file type: {mime} ({ext})")
