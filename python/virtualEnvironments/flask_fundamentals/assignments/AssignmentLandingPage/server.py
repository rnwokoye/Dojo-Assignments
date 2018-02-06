from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html')

# @app.route('/dojos')
# def new_dojos():

# 	return render_template('dojos.html')

@app.route('/dojos/new')
def new():

	return render_template('dojos.html')


@app.route('/user', methods=['POST'])
def create_dojo():
	dojo = request.form ['dojo']
	email = request.form['email']

	print dojo, email


	return redirect('/')

	
# Need help with this redirect. Could ot route to 
#/dojos/new ??




app.run(debug=True)