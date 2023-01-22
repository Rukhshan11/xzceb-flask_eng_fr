from flask import Flask, request, render_template
from machinetranslation import translator

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.english_to_french(textToTranslate)
    return englishText


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    frenchText = translator.french_to_english(textToTranslate)
    return frenchText


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080)
