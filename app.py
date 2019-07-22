from flask import Flask, render_template,request
from flair_predictor import FlairifyMe
import os
port = int(os.environ.get("PORT",5000))

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/flairDetect', methods=['POST'])
def flairDetect():
	redditURL = request.form['redditpost']
	print(redditURL)
	flair = str(FlairifyMe(str(redditURL)))
	print(flair)
	return render_template('home.html',flair=flair)
if __name__ == '__main__':
    app.run()

