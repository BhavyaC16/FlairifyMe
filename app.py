from flask import Flask, render_template,request,jsonify
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
@app.route('/postAnalysis')
def postAnalysis():
	return render_template('analysis.html')
@app.route('/api/resource', methods=['GET'])
def apiFlairDetect():
	redditURL = request.args
	redditURL = str(redditURL)
	redditURL = redditURL[redditURL.find(",")+3:-4]
	print(redditURL)
	flair = str(FlairifyMe(redditURL))
	flairPrediction = {"flair":flair}
	return jsonify(flairPrediction)

if __name__ == '__main__':
    app.run()