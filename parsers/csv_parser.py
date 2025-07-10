# compliance_agent/parsers/csv_parser.py

import pandas as pd
from .base_parser import BaseParser

class CSVParser(BaseParser):
    def parse(self, file_path):
        df = pd.read_csv(file_path)
        return df.to_string(index=False) or "No data found in CSV file."
