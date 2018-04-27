from flask import render_template,flash,session,redirect,url_for,request
from flask_login import login_required,current_user #might not be required

from . import home
from .. import db
from ..models import User, Tutor, Student, Match

import os 
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client=Client(account_sid,auth_token)

# client.messages.create(
# 	to="+15104023847",
# 	from_="+15103301938",
# 	body="Message"
# 	)

@home.route('/')
def homepage():
	return render_template('home/index.html',title="Lets find a match")


@home.route('/dashboard')
@login_required
def dashboard():
	#only display the ones that have not been matched
	if session['userType']=='student':
		tutors = Tutor.query.all()
		# matches = Match.query.filter_by(student_id=current_user.id)
		# print (matches)
		matched_id = db.session.query(Match.tutor_id).filter(Match.student_id==current_user.id)
		return render_template('home/dashboard.html',title="Dashboard",tutors=tutors,matched_id=matched_id)
	else:
		students = Student.query.all()
		matched_id = db.session.query(Match.student_id).filter(Match.tutor_id==current_user.id)
		return render_template('home/dashboard2.html',title="Dashboard",students=students,matched_id=matched_id)

@home.route('/match/<username>',methods=['POST'])
@login_required
def match(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		return redirect(url_for('home.dashboard'))
	#current_user.follow(user)
	print(username)
	client.messages.create(
		#to="+15104023847",
		to=user.phonenumber,
		from_="+15103301938",
		body=current_user.first_name+" would like to connect with you for scholarly needs including "+current_user.needs + ". Contact them at " + str(current_user.phonenumber))

	match = Match(student_id=current_user.id,tutor_id=user.id)
	db.session.add(match)
	db.session.commit()
	return redirect(url_for('home.dashboard'))