import unittest
from main import ResponseCountWordsApi


class ResponseCountWordsApiTest(unittest.TestCase):
    def setUp(self):
        self.cls = ResponseCountWordsApi()

    def test_validate_uri(self):
        uri = 'http://flask-restful-cn.readthedocs.io/en/0.3.5/'
        self.assertTrue(self.cls.is_validate_uri(uri))

    def test_count_words(self):
        pass

if __name__ == '__main__':
    unittest.main()
