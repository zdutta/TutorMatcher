from flask import render_template,flash,session,redirect,url_for
from flask_login import login_required,current_user #might not be required

from . import home
from .. import db
from ..models import User, Tutor, Student, followers

@home.route('/')
def homepage():
	return render_template('home/index.html',title="Lets find a match")


@home.route('/dashboard')
@login_required
def dashboard():
	#only display the ones that have not been matched
	tutors = Tutor.query.all()
	return render_template('home/dashboard.html',title="Dashboard",tutors=tutors)

@home.route('/match/<username>')
@login_required
def match(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		return redirect(url_for('home.dashboard'))
	current_user.follow(user)
	db.session.commit()
	flash('You have matched with {}!'.format(username))
	return redirect(url_for('home.dashboard'))
