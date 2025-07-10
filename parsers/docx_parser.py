# compliance_agent/parsers/docx_parser.py

from docx import Document
from .base_parser import BaseParser

class DOCXParser(BaseParser):
    def parse(self, file_path):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
