from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
app = Flask(__name__)


app.config['SECRET_KEY'] = '7TKUKe09wW1PlrtSL066lsN18uWA7iuO'


@app.route('/')
def home():
    return render_template('index.html', title="Bienvenue chez GrandPy Bot")


@app.route('/_answer')
def answer():
    question = request.args.get('question', 0, type=str)
    question = question.lower()

    stop_words = stopwords.words('french')

    word_tokens = question.split()

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    return jsonify(result=filtered_sentence)


if __name__ == '__main__':
    app.run(debug=True)
