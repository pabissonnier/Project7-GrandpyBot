from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
app = Flask(__name__)


app.config['SECRET_KEY'] = '7TKUKe09wW1PlrtSL066lsN18uWA7iuO'


@app.route('/')
def home():
    return render_template('index.html', title="Bienvenue chez GrandPy Bot")


# Parssing à intégrer en dessous
@app.route('/_answer')
def answer():
    question = request.args.get('question', 0, type=str)
    return jsonify(result=question)


if __name__ == '__main__':
    app.run(debug=True)
