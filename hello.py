# hello.py
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@app.route('/info')
def info():
	user_agent = request.headers.get('User-Agent')
	return render_template('info.html', user_agent=user_agent)

if __name__ == '__main__':
	app.run(host=os.getenv('IP','0.0.0.0'), port=int(os.getenv('PORT',8080)), debug=True)


