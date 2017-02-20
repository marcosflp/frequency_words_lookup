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

The word counter resource can be accessed by: http://localhost:5000/wordcounter
Receives two parameters in the querystring
1. uri
2. word

Example:
```
http://localhost:5000/wordcounter?uri=https://news.ycombinator.com/item?id=13683110&word=http
```
