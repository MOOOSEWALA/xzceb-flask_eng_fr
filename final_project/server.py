from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
     english_text = request.json['english_text']
    french_text = english_to_french(english_text)
    return {'french_text': french_text}

    
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
   french_text = request.json['french_text']
    english_text = french_to_english(french_text)
    return {'english_text': english_text}

    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
