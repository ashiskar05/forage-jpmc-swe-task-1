import unittest
from client3 import getDataPoint,get_random_quote
from unittest.mock import patch

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
            ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEquals(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2 ))


    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
            ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEquals(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2 ))


    """ ------------ Add more unit tests ------------ """
    @patch("urllib.request.urlopen")
    def test_get_random_quote(self, mock_urlopen):
        # Set up mock response
        mock_urlopen.return_value.read.return_value = b'{"quote": "Mock Quote"}'
        # Call the function
        result = get_random_quote()
        # Check if the result is as expected
        self.assertEquals(result,{"quote": "Mock Quote"})




if __name__ == '__main__':
    unittest.main()
