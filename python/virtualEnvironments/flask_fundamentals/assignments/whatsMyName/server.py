from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():

	return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

	# name =request.form['name']
	# email = request.form['email']
	
	print request.form

	return redirect('/')


app.run(debug=True)

