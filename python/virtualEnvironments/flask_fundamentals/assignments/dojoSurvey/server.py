from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():

	return render_template('/index.html')


@app.route('/result', methods=['POST'])
def result():
	name = request.form['name']
	location = request.form['Dojo Location']
	language = request.form['Favorite Language']
	comments = request.form['comments']
	print type(request.form)
	

	return render_template('/result.html', Name=name, Location=location, Language=language, Comments=comments )


# @app.route('/surverdata')
# def surverdata():

# 	return render_template('/surverdata.html')


app.run(debug=True)
