from flask import Flask, render_template, request, redirect
app = Flask(__name__) 


@app.route('/')
def index():
	
	return render_template("index.html")

@app.route('/about')
def about():

	return render_template("about.html")

@app.route('/user', methods=['POST'])
def create_user_profile():
	print "Got post info"
	name = request.form['name']
	email = request.form['email']
	userID = request.form['userID']

	print name, email, userID
	return redirect('/portfolio')

@app.route("/portfolio")
def portfolio():

	return render_template("portfolio.html")


@ app.route("/projects")
def projects():


	return render_template("projects.html")


app.run(debug=True)


#Solution Given
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/projects')
# def projects():
#     my_projects = ['Ninja Gold', 'Great Number Game', 'Disappearing Ninjas', 'Dojo Survey']
#     return render_template('projects.html', projects=my_projects)

# @app.route('/about')
# def about():
#     return render_template('about.html')

# app.run(debug=True)
