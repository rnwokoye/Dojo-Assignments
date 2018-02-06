from flask import Flask, session, render_template, redirect, request, flash
app = Flask(__name__)

@app.route('/')
def index():

	return render_template('/index.html')

@app.route('/register', methods=['POST'])
def register():
	errors = []

	#check email
	if (len(request.form['email'])) < 1:
		errors.append('Email cannot be blank')

	#check email
	if (len(request.form['email'])) < 1:
		errors.append('Email cannot be blank')

	#check email
	if (len(request.form['email'])) < 1:
		errors.append('Email cannot be blank')

	#check email
	if (len(request.form['email'])) < 1:
		errors.append('Email cannot be blank')








	
	print request.form 
	return redirect('/')




app.run(debug=True)