from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends1db')
@app.route('/')
def index():
	
	query = "SELECT * from friends"
	all_friends = mysql.query_db(query) 


	return render_template('index.html', Squad=all_friends)

@app.route('/new', methods=['POST'])
def new():


	query = "INSERT INTO friends (name, age, friend_since, created_at, updated_at) VALUES (:name, :age, :friend_since, NOW(), NOW())"

	data = {
		'name' : request.form['name'], 
		'age' : request.form['age'],
		'friend_since' : request.form['friend_since']
	}
	

	mysql.query_db(query, data)

	return redirect('/')


app.run(debug=True)
