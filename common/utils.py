import re


def is_valid_uri(uri):
    """
    Return True if the uri is valid.
    Use a regex that is used to compare if the uri looks like with a real http(s) uri
    :param uri: Any uri. E.g. http://flask-restful-cn.readthedocs.io/en/0.3.5/index.html
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


def clean_word(word):
    cleaned_word = re.sub('[^A-Za-z]+', '', word)

    return cleaned_word
