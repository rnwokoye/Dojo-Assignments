from flask import flask, render_templates, request, redirect
app = Flask(__name__)

@app.route('/')
def index.html():

	return render_templates('index.html')
	


