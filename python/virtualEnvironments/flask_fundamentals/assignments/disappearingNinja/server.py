from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template('/index.html')

@app.route('/ninja')
def ninjas():

	return render_template('ninja.html')

@app.route('/ninja/<color>')
def show_ninja_color(color):
	print color

	if color=='blue':
		return render_template('my_ninja.html', name = 'leonardo')
	elif color=='orange':
		return render_template('my_ninja.html', name = 'michelangelo')
	elif color=='red':
		return render_template('my_ninja.html',name = 'raphael')
	elif color=='purple':
		return render_template('my_ninja.html',name = 'donatello')

	else:
	 	return render_template('my_ninja.html', name = 'notapril')


app.run(debug=True)