## Requirements

* Python 2.7.x


## Installation

```bash
$ git clone https://github.com/marcosflp/frequency_words_lookup.git frequency_words_lookup
$ cd frequency_words_lookup
$ pip install -r requirements.txt
```


## Running the development server

```bash
$ python app.py
```


## Usage

The word counter resource can be accessed by: http://localhost:5000/wordcounter. 
Gets two parameters in the querystring

1. uri
2. word

Example:
```
http://localhost:5000/wordcounter?uri=https://news.ycombinator.com/item?id=13683110&word=http
```

Uri with querystring must be encoded before submitted. Example:

uri with parameters on querystring: http://flask-restful-cn.readthedocs.io/en/0.3.5/search.html?q=rest&check_keywords=yes&area=default

usage
```
http://localhost:5000/wordcounter?uri=http%3A%2F%2Fflask-restful-cn.readthedocs.io%2Fen%2F0.3.5%2Fsearch.html%3Fq%3Drest%26check_keywords%3Dyes%26area%3Ddefault&word=rest
```
