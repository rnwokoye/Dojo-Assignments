
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
	print username
	printcopy id
    return render_template("user.htm