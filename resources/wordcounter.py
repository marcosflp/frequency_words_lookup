# -*- coding: utf-8 -*-

import requests
from flask import request
from flask_restful import Resource
from lxml import html
from stop_words import get_stop_words
from common.utils import is_valid_uri, clean_word


class WordCounterApi(Resource):

    def __init__(self):
        super(WordCounterApi, self).__init__()
        self.error = {'error': False,
                      'messages': [],
                      'status': 404}

    def get(self):
        response = self.get_response_from_uri('GET', request.args.get('uri'))
        words_found_list = self.get_words(response.content, request.args.get('word'))

        if self.error.get('error'):
            return self.error_handler()

        return {'uri': request.args.get('uri'),
                'word': request.args.get('word') or '',
                'number_of_words_found': len(words_found_list),
                'data': [{'words_found': words_found_list}]}

    def get_response_from_uri(self, http_verb, uri):
        """ Return the number of words found in a response """

        if not is_valid_uri(request.args.get('uri')):
            return self.set_error('The URI {} is invalid'.format(uri), 404)

        try:
            response = requests.request(http_verb, uri)
        except Exception as e:
            # retry once, it could be a momentary overloaded server?
            try:
                response = requests.request(http_verb, uri)
            except Exception as e:
                return self.set_error('An error occurred while trying to access {}'.format(uri), 404)

        if response.status_code != 200:
            return self.set_error('An error occurred while trying to access {}'.format(uri), response.status_code)

        return response

    def get_words(self, html_content, search_word):
        """ Return a list with all words found on an html content """

        # parse the html tree to string by removing all html elements
        html_tree = html.fromstring(html_content)
        text = html_tree.xpath('string()')

        # remote stop words(pt) like 'a', 'em', 'quem', 'este'...
        stop_words = get_stop_words('portuguese')
        word_list = []
        for w in text.replace('\n', ' ').strip().split():
            cleaned_w = clean_word(w)
            if cleaned_w not in stop_words:
                word_list.append(cleaned_w)

        return [w for w in word_list if search_word.lower() in w.lower()]

    def error_handler(self):
        return {'message': self.error.get('messages')}, self.error.get('status')

    def set_error(self, message, status):
        self.error['error'] = True
        self.error['messages'].append(message)
        self.error['status'] = status
