from flask import Flask, render_template
from random import randrange
from test import Student

app = Flask(__name__)

TITLES = ["Hello Python", "'Sup", "Contents"]

@app.route("/")
def index():
	title = TITLES[randrange(len(TITLES))]
	return render_template("index.html", title=title)

@app.route("/home")
def home():
	student1 = Student("slim shady")
	student1.introduce()
	return render_template("home.html")

@app.route("/test")
def something():
	return "test"

app.run(debug=True)