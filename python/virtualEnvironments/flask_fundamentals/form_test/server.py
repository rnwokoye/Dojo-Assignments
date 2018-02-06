from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#our index route below will handle rendering our form
@app.route('/')
def index():
	return render_template("index.html")


@app.route('/show')
def show_user():

	return render_template('user.html', name='Jay', email='Kpatel@codingdojo.com')

#this route will handle our form submission
# Notice how we have defined which http methods 
#are allowed by this second route.

# @app.route('/user')
# def success():

# 	#return render_template("user.html")

@app.route('/success')
def success():
	return render_template("success.html")

@app.route('/user', methods=['POST'])
def show_user_profile():
#def create_user():
	print "Got post info"
	#these following two lines will be discussed more later

	name = request.form['username']
	email = request.form['email']
	#the following line redirects to root
	print name, email		#This prints the form input dta in terminal window
	#print request.form
	print name
	return redirect('/success.html')
	#return render_template('success.html')
	#return render_template("user.html")	

app.run(debug=True)


