from flask import Flask, render_template, request
from translator import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/french-to-english', methods=['POST'])
def translate_french_to_english():
    text = request.form['text']
    translated_text = french_to_english(text)
    return render_template('index.html', translated_text=translated_text)

@app.route('/english-to-french', methods=['POST'])
def translate_english_to_french():
    text = request.form['text']
    translated_text = english_to_french(text)
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run()
