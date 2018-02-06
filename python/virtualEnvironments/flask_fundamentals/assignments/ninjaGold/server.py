from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'junior'

@app.route('/')
def index():
	if 'yourGold' not in session:
		session['yourGold'] = 0

	if 'activity' not in session:
		session['activity'] = []

	return render_template('index.html')


@app.route('/process_gold', methods=['POST'])
def process_gold():
	
	print request.form['location']
	if request.form['location'] == 'Farm':
		goldEarned = random.randint(10, 20)
		message = "went to {} and earned {} gold".format(request.form['location'], goldEarned)
		print message
		session['activity'].append(message)
		session['yourGold'] = session['yourGold'] + goldEarned

	elif request.form['location'] == 'Cave':
		goldEarned = random.randint(5, 10)
		message = "went to {} and earned {} gold".format(request.form['location'], goldEarned)
		print message
		session['activity'].append(message)
		session['yourGold'] = session['yourGold'] + goldEarned

	
	elif request.form['location'] == 'House':
		goldEarned = random.randint(2, 5)
		message = "went to {} and earned {} gold".format(request.form['location'], goldEarned)
		print message
		session['activity'].append(message)
		session['yourGold'] = session['yourGold'] + goldEarned

	
	elif request.form['location'] == 'Casino':
		goldEarned = random.randint(-50, 50)
		if goldEarned > 0:
			winlose = "earned"
		else:
			winlose = "lost"
		message = "went to {} and {} {} gold".format(request.form['location'], winlose, abs(goldEarned))
		session['activity'].append(message)
		print message
		session['yourGold'] = session['yourGold'] + goldEarned
	return redirect('/')



app.run(debug=True)