from flask import Flask, render_template, request, jsonify

import sentences_list
import random
from extraction import Extraction
from parssing import Parssing
import wikipedia
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
    try:
        url_googleaddress = Extraction.get_urladdress(datas_extraction, filtered_sentence)
        googleapi_data = Extraction.get_googleapi_data(datas_extraction, url_googleaddress)
        address_location = Extraction.get_address(datas_extraction, googleapi_data)
        random_sentence = random.choice(sentences_list.sentences_address)
        address_sentence = random_sentence+address_location
        return jsonify(result=address_sentence)
    except (ValueError, TypeError):
        return jsonify(result="Mince, je ne trouve pas, essaye une autre adresse :)")


@app.route('/_map')
def map():
    question = request.args.get('question', 0, type=str)
    filtered_sentence = Parssing.get_main_words(datas_management, question)
    url_googleaddress = Extraction.get_urladdress(datas_extraction, filtered_sentence)
    googleapi_data = Extraction.get_googleapi_data(datas_extraction, url_googleaddress)
    lat = Extraction.get_lat(datas_extraction, googleapi_data)
    lng = Extraction.get_lng(datas_extraction, googleapi_data)
    if lat is None or lng is None:
        return jsonify(result="")
    else:
        url_googlemap = Extraction.get_urlmap(datas_extraction, filtered_sentence, lat, lng)
        return jsonify(result=url_googlemap)


@app.route('/_wiki')
def wiki():
    question = request.args.get('question', 0, type=str)
    filtered_sentence = Parssing.get_main_words(datas_management, question)
    first_word = Parssing.wiki_firstword(datas_management, filtered_sentence)
    try:
        sentence_wiki = Extraction.wiki_datas(datas_extraction, first_word)
        random_sentence = random.choice(sentences_list.sentences_wiki)
        result_wiki = random_sentence+sentence_wiki
        return jsonify(result=result_wiki)
    except wikipedia.exceptions.DisambiguationError:
        return jsonify(result="Je peux trouver des infos mais il y a beaucoup de choses avec le même nom, peux-tu préciser s'il te plait ?")
    except wikipedia.exceptions.PageError:
        return jsonify(result="Hum, ça ne me dit vraiment rien...")


@app.route('/_wikilink')
def wikilink():
    question = request.args.get('question', 0, type=str)
    filtered_sentence = Parssing.get_main_words(datas_management, question)
    first_word = Parssing.wiki_firstword(datas_management, filtered_sentence)
    try:
        link_wiki = Extraction.wiki_link(datas_extraction, first_word)
        return jsonify(result=link_wiki)
    except wikipedia.exceptions.DisambiguationError:
        pass
    except wikipedia.exceptions.PageError:
        pass


if __name__ == '__main__':
    app.run(debug=True)
