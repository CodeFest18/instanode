import flask
import time
import requests
import threading

app = flask.Flask(__name__)

@app.route('/')
def home():
	return flask.render_template('home.html')

@app.route('/gui')
def gui():
	return flask.render_template('gui.html')

if __name__ == '__main__':
	app.run(debug=True)
