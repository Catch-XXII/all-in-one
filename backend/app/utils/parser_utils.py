# app/utils/parser_utils.py

from collections import Counter

from bs4 import BeautifulSoup


class HTMLStructureAnalyzer:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")

    def get_document_structure(self) -> dict:
        structure = {
            "has_html": self.soup.html is not None,
            "has_head": self.soup.head is not None,
            "has_body": self.soup.body is not None,
            "has_main": self.soup.find("main") is not None,
            "has_footer": self.soup.find("footer") is not None,
        }
        return structure

    def get_tag_counts(self) -> dict:
        tags = [tag.name for tag in self.soup.find_all()]
        return dict(Counter(tags))
