from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask('Web Translator')

@app.route('/')
def renderIndexPage():
	return render_template('index.html')

@app.route("/englishtofrench")
def englishtofrench():
	
	texttotranslate = request.args.get('texttotranslate')
	
	french_text= translator.english_to_french(texttotranslate)
      
	return french_text

@app.route("/frenchtoenglish")
def frenchtoenglish():
	
	texttotranslate = request.args.get('texttotranslate')
	
	english_text= translator.french_to_english(texttotranslate)
      
	return english_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
