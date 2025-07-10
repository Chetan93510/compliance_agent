# compliance_agent/parsers/xlsx_parser.py

import pandas as pd
from .base_parser import BaseParser

class XLSXParser(BaseParser):
    def parse(self, file_path):
        dfs = pd.read_excel(file_path, sheet_name=None)
        content = ""
        for sheet_name, df in dfs.items():
            content += f"\nSheet: {sheet_name}\n"
            content += df.to_string(index=False) + "\n"
        return content or "No data found in Excel file."
