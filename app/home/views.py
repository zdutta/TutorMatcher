from flask import render_template,flash,session,redirect,url_for,request
from flask_login import login_required,current_user #might not be required

from . import home
from .. import db
from ..models import User, Tutor, Student, Match

@home.route('/')
def homepage():
	return render_template('home/index.html',title="Lets find a match")


@home.route('/dashboard')
@login_required
def dashboard():
	#only display the ones that have not been matched

	tutors = Tutor.query.all()
	# matches = Match.query.filter_by(student_id=current_user.id)
	# print (matches)
	matched_id = db.session.query(Match.tutor_id).filter(Match.student_id==current_user.id)
	return render_template('home/dashboard.html',title="Dashboard",tutors=tutors,matched_id=matched_id)

@home.route('/match/<username>',methods=['POST'])
@login_required
def match(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		return redirect(url_for('home.dashboard'))
	#current_user.follow(user)
	match = Match(student_id=current_user.id,tutor_id=user.id)
	db.session.add(match)
	db.session.commit()
	flash('You have matched with {}!'.format(username))
	return redirect(url_for('home.dashboard'))