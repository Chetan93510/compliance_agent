# compliance_agent/parsers/image_parser.py

from PIL import Image
import pytesseract
from .base_parser import BaseParser

class ImageParser(BaseParser):
    def parse(self, file_path):
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text or "No text found in image."
