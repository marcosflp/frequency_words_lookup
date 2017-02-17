import re
import requests
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ResponseCountWordsApi(Resource):
    def get(self):
        self.is_validate_uri(request.args.get('uri'))

        return {'uri': request.args.get('uri'),
                'word': request.args.get('word') or '',
                'number_of_words': self.count_words(request.args.get('word'))}

    def is_validate_uri(self, uri):
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

    def count_words(self, uri, word):
        pass


api.add_resource(ResponseCountWordsApi, '/', methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)
