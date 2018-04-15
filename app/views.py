from flask import render_template
from app import app 

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/signUp")
def signUp():
# 	#readingthe posted values from the form
# 	_name = request.form['input name']
# 	_email = request.form['inputEmail']
# 	_password = request.form['inputPassword']
# 	if _name and _email and _password:
# 		return json.dumps({'html':'<span>All fields are valid</span>'})
# 	else:
# 		return json.dumps({'html':'<span>Enter the required fields</span>'})
	return render_template('signup.html')



@app.route("/login") #page that handles login 
def login():
	return render_template('login.html')

@app.route("/profile") #page that has profile information and includes the ability to configure
def profile():
	return render_template('profile.html')

@app.route("/activity") #swiping/selection page
def activity():
	return render_template('activity.html')

@app.route("/matches") #page for messaging matches
def matches():
	return "Present messaging with matches"