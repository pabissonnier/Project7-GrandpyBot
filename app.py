from flask import Flask, render_template, request, jsonify

import sentences_list
import random
from extraction import Extraction
from parssing import Parssing
app = Flask(__name__)


app.config['SECRET_KEY'] = '7TKUKe09wW1PlrtSL066lsN18uWA7iuO'

# Instances creation
datas_extraction = Extraction()
datas_management = Parssing()


@app.route('/')
def home():
    return render_template('index.html', title="Bienvenue chez GrandPy Bot")


@app.route('/_answer')
def answer():
    question = request.args.get('question', 0, type=str)
    return jsonify(result=question)


@app.route('/_address')
def address():
    question = request.args.get('question', 0, type=str)
    filtered_sentence = Parssing.get_main_words(datas_management, question)
    url_googleaddress = Extraction.get_urladdress(datas_extraction, filtered_sentence)
    googleapi_data = Extraction.get_googleapi_data(datas_extraction, url_googleaddress)
    address_location = Extraction.get_address(datas_extraction, googleapi_data)
    random_sentence = random.choice(sentences_list.sentences_address)
    address_sentence = random_sentence+address_location
    return jsonify(result=address_sentence)


@app.route('/_map')
def map():
    question = request.args.get('question', 0, type=str)
    filtered_sentence = Parssing.get_main_words(datas_management, question)
    url_googleaddress = Extraction.get_urladdress(datas_extraction, filtered_sentence)
    googleapi_data = Extraction.get_googleapi_data(datas_extraction, url_googleaddress)
    lat = Extraction.get_lat(datas_extraction, googleapi_data)
    lng = Extraction.get_lng(datas_extraction, googleapi_data)
    url_googlemap = Extraction.get_urlmap(datas_extraction, filtered_sentence, lat, lng)
    return jsonify(result=url_googlemap)


@app.route('/_wiki')
def wiki():
    question = request.args.get('question', 0, type=str)
    filtered_sentence = Parssing.get_main_words(datas_management, question)
    first_word = Parssing.wiki_firstword(datas_management, filtered_sentence)
    sentence_wiki = Extraction.wiki_datas(datas_extraction, first_word)
    link_wiki = Extraction.wiki_link(datas_extraction, first_word)
    random_sentence = random.choice(sentences_list.sentences_wiki)
    result_wiki = random_sentence+sentence_wiki+link_wiki
    return jsonify(result=result_wiki)


if __name__ == '__main__':
    app.run(debug=True)
