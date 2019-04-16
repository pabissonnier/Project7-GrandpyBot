from flask import Flask, render_template, request, jsonify
import json
import urllib.request
import wikipedia
import sentences_list
import random
app = Flask(__name__)


app.config['SECRET_KEY'] = '7TKUKe09wW1PlrtSL066lsN18uWA7iuO'


def get_main_words(question):
    question = question.lower()

    word_tokens = question.split()

    with open('stopwords.json', encoding='utf-8') as json_file:
        stopwords = json.load(json_file)

        filtered_list = [w for w in word_tokens if not w in stopwords]

        filtered_sentence = '+'.join(filtered_list)
        return filtered_sentence


def get_googleapi_data(url_googleaddress):
    googleapi_json = urllib.request.urlopen(url_googleaddress)
    googleapi_read = googleapi_json.read()
    googleapi_data = json.loads(googleapi_read.decode("utf-8"))
    return googleapi_data


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
    filtered_sentence = get_main_words(question)

    url_googleaddress = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                    "query={0}&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0".format(filtered_sentence)

    try:
        googleapi_data = get_googleapi_data(url_googleaddress)
        assert googleapi_data is True

        for items in googleapi_data["results"]:
            address_location = items["formatted_address"]
            random_sentence = random.choice(sentences_list.sentences)
            address_sentence = random_sentence+address_location
            return jsonify(result=address_sentence)
    except AssertionError:
            return jsonify(result="Oops, je ne trouve pas l'adresse... Essaie autre chose :)")


@app.route('/_map')
def map():
    question = request.args.get('question', 0, type=str)
    filtered_sentence = get_main_words(question)

    url_googleaddress = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                    "query={0}&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0".format(filtered_sentence)

    googleapi_data = get_googleapi_data(url_googleaddress)

    for items in googleapi_data["results"]:
        lat = items["geometry"]["location"]["lat"]
        lng = items["geometry"]["location"]["lng"]

        url_googlemap = "https://maps.googleapis.com/maps/api/staticmap?center={0}&zoom=13" \
                        "&size=400x300&maptype=roadmap" \
                        "&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0" \
                        "&format=png&visual_refresh=true" \
                        "&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C3{1},{2}".format(filtered_sentence, lat, lng)

        return jsonify(result=url_googlemap)


@app.route('/_wiki')
def wiki():
    question = request.args.get('question', 0, type=str)
    filtered_sentence = get_main_words(question)
    words_list = filtered_sentence.split('+')
    first_word = words_list[0]
    wikipedia.set_lang('fr')
    try:
        sentence_wiki = wikipedia.summary(first_word, sentences=1)
        link_wiki_api = wikipedia.page(first_word).url
        assert wikipedia.page is True
        link_wiki = """
        <html><head></head><body><a href={0}>Si tu veux en savoir plus</a></body></html>""".format(link_wiki_api)
        result_wiki = sentence_wiki+link_wiki
        return jsonify(result=result_wiki)
    except IndexError:
        return jsonify(result="Je me suis emmelé les pinceaux...Essaye avec une autre orthographe")
    except TypeError:
        return jsonify(result="Je me suis emmelé les pinceaux...Essaye avec une autre orthographe")
    except AssertionError:
        return jsonify(result="Je me suis emmelé les pinceaux...Essaye avec une autre orthographe")


if __name__ == '__main__':
    app.run(debug=True)
