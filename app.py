from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
import json
import urllib.request
app = Flask(__name__)


app.config['SECRET_KEY'] = '7TKUKe09wW1PlrtSL066lsN18uWA7iuO'


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
    question = question.lower()

    word_tokens = question.split()

    with open('stopwords.json', encoding='utf-8') as json_file:
        stopwords = json.load(json_file)

        filtered_list = [w for w in word_tokens if not w in stopwords]

        filtered_sentence = '+'.join(filtered_list)

        url_googleaddress = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                        "query={0}&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0".format(filtered_sentence)

        googleapi_json = urllib.request.urlopen(url_googleaddress)
        googleapi_read = googleapi_json.read()
        googleapi_data = json.loads(googleapi_read.decode("utf-8"))

        for items in googleapi_data["results"]:
            address_location = items["formatted_address"]
            return jsonify(result=address_location)


@app.route('/_map')
def map():
    question = request.args.get('question', 0, type=str)
    question = question.lower()

    word_tokens = question.split()

    with open('stopwords.json', encoding='utf-8') as json_file:
        stopwords = json.load(json_file)

        filtered_list = [w for w in word_tokens if not w in stopwords]

        filtered_sentence = '+'.join(filtered_list)

        url_googleaddress = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                        "query={0}&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0".format(filtered_sentence)

        googleapi_json = urllib.request.urlopen(url_googleaddress)
        googleapi_read = googleapi_json.read()
        googleapi_data = json.loads(googleapi_read.decode("utf-8"))

        for items in googleapi_data["results"]:
            lat = items["geometry"]["location"]["lat"]
            lng = items["geometry"]["location"]["lng"]

            url_googlemap = "https://maps.googleapis.com/maps/api/staticmap?center={0}&zoom=13" \
                            "&size=400x300&maptype=roadmap" \
                            "&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0" \
                            "&format=png&visual_refresh=true" \
                            "&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C3{1},{2}".format(filtered_sentence, lat, lng)

            return jsonify(result=url_googlemap)


""""@app.route('/_wiki')
def address():
    question = request.args.get('question', 0, type=str)
    question = question.lower()

    word_tokens = question.split()

    with open('stopwords.json', encoding='utf-8') as json_file:
        stopwords = json.load(json_file)

        filtered_list = [w for w in word_tokens if not w in stopwords]

        filtered_sentence = '+'.join(filtered_list)

        url_wiki = "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro" \
                   "&titles={0}&format=jsonfm".format(filtered_sentence)

        wiki_json = urllib.request.urlopen(url_wiki)
        wiki_read = wiki_json.read()
        wiki_data = json.loads(wiki_read.decode("utf-8"))

        for items in googleapi_data["results"]:
            address_location = items["formatted_address"]
            return jsonify(result=address_location)"""



if __name__ == '__main__':
    app.run(debug=True)
