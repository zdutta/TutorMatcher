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
	return render_template('home/dashboard.html',title="Dashboard")

@home.route('/match/<username>')
@login_required
def match(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		flash('Person does not exist')
	current_user.follow(user)
	flash('You have matched with {}!'.format(username))
	return redirect(url_for('home.dashboard'))



# 	@app.route('/follow/<username>')
# @login_required
# def follow(username):
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         flash('User {} not found.'.format(username))
#         return redirect(url_for('index'))
#     if user == current_user:
#         flash('You cannot follow yourself!')
#         return redirect(url_for('user', username=username))
#     current_user.follow(user)
#     db.session.commit()
#     flash('You are following {}!'.format(username))
#     return redirect(url_for('user', username=username))

# @app.route('/unfollow/<username>')
# @login_required
# def unfollow(username):
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         flash('User {} not found.'.format(username))
#         return redirect(url_for('index'))
#     if user == current_user:
#         flash('You cannot unfollow yourself!')
#         return redirect(url_for('user', username=username))
#     current_user.unfollow(user)
#     db.session.commit()
#     flash('You are not following {}.'.format(username))
#     return redirect(url_for('user', username=username))