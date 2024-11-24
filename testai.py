import unittest
from main import *

class TestCrawl(unittest.TestCase):

    def test_crawl_dict(self):
        data = crawl("pigu", "dict")
        self.assertIsInstance(data, dict)
        self.assertIn("title", data)
        self.assertIn("price", data)

    def test_crawl_csv(self):
        filename = crawl("pigu", "csv")
        self.assertEqual(filename, "output.csv")

    def test_crawl_invalid_source(self):
        with self.assertRaises(ValueError):
            crawl("Nezinomas", "dict")

    def test_crawl_invalid_format(self):
        with self.assertRaises(ValueError):
            crawl("pigu", "Netinkamas_formatas")

    def test_save_as_csv(self):
        data = {"title": "Test Product", "price": "10 EUR"}
        filename = save_as_csv(data)
        self.assertEqual(filename, "output.csv")

if __name__ == "__main__":
    unittest.main()