from flask import Flask, render_template,request, make_response
from flair_predictor import FlairifyMe, FlairDetect
import json
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
	predicted_flair = str(FlairifyMe(str(redditURL)))
	actual_flair = str(FlairDetect(str(redditURL)))
	print(predicted_flair, actual_flair)
	return render_template('home.html', predicted_flair = predicted_flair, actual_flair = actual_flair)
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
	flairPrediction = {'status': 'successful', 'status_code': 200, 'result':{'flair':flair}}
	return json.dumps(flairPrediction)
@app.errorhandler(404)
def not_found(error):
	return make_response(json.dumps({'status': 'failed', 'status_code': 404, 'result': {'error': 'Not found'}}))
@app.errorhandler(500)
def internal_server_error(error):
	return make_response(json.dumps({'status': 'failed', 'status_code': 500, 'error': '500: Incorrect request format'}),500)
if __name__ == '__main__':
    app.run()
