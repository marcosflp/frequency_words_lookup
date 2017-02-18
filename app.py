from flask import Flask
from flask_restful import Api
from resources.wordcounter import WordCounterApi
from settings import DEBUG_ON

app = Flask(__name__)
api = Api(app)

api.add_resource(WordCounterApi, '/wordcounter', methods=['GET'])

if __name__ == '__main__':
    app.run(debug=DEBUG_ON)
