import unittest
from api_client import get_new_image

class TestApiClient(unittest.TestCase):
    def test_get_new_image_returns_string_or_none(self):
        url = get_new_image()
        self.assertTrue(url is None or isinstance(url, str))

if __name__ == '__main__':
    unittest.main()
