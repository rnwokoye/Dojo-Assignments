from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  	return render_template("index.html")

@app.route('/users/<username>/<email>')
def show_user_profile(username, email):
	
	print username, email
	my_data = username, email
	print type(my_data)

  
   	return render_template('user.html',username='my_data')

app.run(debug=True) # run our server



# from flask import Flask, render_template, request, redirect
# app = Flask(__name__)

# @app.route('/')
# def index():
#   return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#    print "Got Post Info"
   
#    name = request.form['name']
#    email = request.form['email']
   
#    #return redirect('/')
#    return render_template('/success.html')

# app.run(debug=True) # run our server
