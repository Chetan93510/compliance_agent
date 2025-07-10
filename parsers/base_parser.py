# compliance_agent/parsers/base_parser.py

from abc import ABC, abstractmethod

class BaseParser(ABC):
    @abstractmethod
    def parse(self, file_path):
        """
        Parse the file and return text content.
        """
        pass
