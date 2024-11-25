import unittest
from karolis_s_mod1_atsiskaitymas.main import crawl, crawl_eurovaistine, save_as_csv

class TestCrawl(unittest.TestCase):

    def test_scrape_eurovaistine(self):
        data = crawl_eurovaistine ()
        self.assertIsInstance (data, list)
        self.assertGreater (len (data), 0)
        self.assertIn ("title", data[0])
        self.assertIn ("priceContainer", data[0])

    def test_crawl_dict(self):
        data = crawl ('eurovaistine', 'dict')
        self.assertIsInstance (data, list)

    def test_crawl_csv(self):
        filename = crawl ('eurovaistine', 'csv')
        self.assertEqual (filename, "output.csv")

    def test_save_as_csv(self):
        data = [{"title": "Test Product", "priceContainer": "10 EUR"}]
        filename = save_as_csv (data)
        self.assertEqual (filename, "output.csv")

if __name__ == "__main__":
    unittest.main()