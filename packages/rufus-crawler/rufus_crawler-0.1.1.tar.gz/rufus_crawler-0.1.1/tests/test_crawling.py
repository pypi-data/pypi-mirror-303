# tests/test_crawling.py
import unittest
from rufus.client import RufusClient
from rufus.content_filter import ContentFilter
import os

class TestRufus(unittest.TestCase):
    def test_crawl(self):
        client = RufusClient()
        url = "https://www.uta.edu/admissions/apply/graduate"
        client.crawl(url, depth=1)
        self.assertTrue(os.path.exists(client.base_folder))

    def test_content_filter(self):
        content_filter = ContentFilter("fake_key")
        filtered = content_filter.filter_content("Test instruction", [{"URL": "test.com", "content": "This is a test content"}])
        self.assertTrue(len(filtered) > 0)

if __name__ == "__main__":
    unittest.main()
