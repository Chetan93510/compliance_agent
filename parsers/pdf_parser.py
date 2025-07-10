# compliance_agent/parsers/pdf_parser.py

import pdfplumber
from .base_parser import BaseParser

class PDFParser(BaseParser):
    def parse(self, file_path):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text or "No text found in PDF."
