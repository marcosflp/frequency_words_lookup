import re

import requests
from flask import Flask, request
from flask_restful import Resource, Api
from lxml import html
from stop_words import get_stop_words

app = Flask(__name__)
api = Api(app)


class ResponseCountWordsApi(Resource):

    def get(self):
        self.is_valid_uri(request.args.get('uri'))
        words_found = self.search_word('GET', request.args.get('uri'), request.args.get('word'))

        return {'uri': request.args.get('uri'),
                'word': request.args.get('word') or '',
                'number_of_words_found': len(words_found),
                'data': words_found}

    def is_valid_uri(self, uri):
        """
        Return True if the uri is valid.
        Use a regex that is used to compare if the uri looks like with a real http(s) uri
        """

        regex = re.compile(
                r'^(?:http)s?://'
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                r'localhost|'
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                r'(?::\d+)?'
                r'(?:/?|[/?]\S+)$', re.I)

        is_match = regex.match(uri)

        if is_match:
            return True
        else:
            return False

    def search_word(self, http_verb, uri, word):
        """ Return the number of words found in a response """

        try:
            response = requests.request(http_verb, uri)
        except Exception as e:
            # retry once, it could be a momentary overloaded server?
            try:
                response = requests.request(http_verb, uri)
            except Exception as e:
                raise e

        if response.status_code != 200:
            # TODO: handler message error
            raise

        # get only strings from a response
        # parse the html tree to string by removing all html elements
        html_tree = html.fromstring(response.content)
        text = html_tree.xpath("string()")

        # remote stop words(pt) like 'a', 'em', 'quem', 'este'...
        stop_words = get_stop_words('portuguese')
        word_list = [w for w in text.replace('\n', ' ').strip().split() if word not in stop_words]

        return [w for w in word_list if word.lower() in w.lower()]

api.add_resource(ResponseCountWordsApi, '/', methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
