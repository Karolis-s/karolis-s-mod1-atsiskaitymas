import unittest
from main import gesintuvu_kainos
from unittest.mock import patch

class TestGesintuvoKainos(unittest.TestCase):
    @patch("requests.get")
    def test_gesintuvo_kainos(self, mock_get):
        mock_get.return_value.status_code = 200

        data = gesintuvu_kainos(url = "https://www.gesinu.lt", output_format = "dict")
        self.assertIsInstance(data, dict)
        self.assertEqual((data["gesintuvai"]), 3)
        self.assertEqual((data["gesintuvai"][0]), "Gesintuvas miltelinis 6 kg")
        self.assertEqual(data["prices"][0], "€35.00")





if __name__ == '__main__':
    unittest.main()

