import unittest
from common.utils import is_valid_uri
from resources.wordcounter import WordCounterApi
from os import path
from settings import ROOTDIR


class WordCounterApiTest(unittest.TestCase):
    def setUp(self):
        self.cls = WordCounterApi()

    def test_validate_uri(self):
        uri = 'http://flask-restful-cn.readthedocs.io/en/0.3.5/'
        self.assertTrue(is_valid_uri(uri))

    def test_count_words(self):
        with open(path.join(ROOTDIR, 'fixtures/page.html')) as f:
            html_content = f.read()

        words_found_list = self.cls.get_words(html_content, 'flask')
        self.assertEqual(len(words_found_list), 32)

if __name__ == '__main__':
    unittest.main()
