from flask import render_template,flash,url_for,redirect, jsonify, request,session
from flask_login import login_required, current_user #might not be required

from . import matches
from ..models import User, Tutor, Student, Match, Messages
from .. import db
import pusher
from flask_sqlalchemy import SQLAlchemy 

pusher_client = pusher.Pusher(
  app_id='516589',
  key='b67e1b7dd4b245e4a5c9',
  secret='c95b217dade1f6bffe25',
  cluster='us2',
  ssl=True
)

@matches.route('/messages')
@login_required
def messages():
	messages = Messages.query.filter_by()
	matched = None
	if session['userType'] == 'student':
		matches = Match.query.filter_by(student_id=current_user.id).first()
	else:
		matches = Match.query.filter_by(tutor_id=current_user.id).first()

	return render_template('matches/messages.html', title="Messages", messages=messages)

@matches.route('/unmatch/<username>')
@login_required
def unmatch(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		return redirect(url_for('matches.messages'))
	Match.query.filter_by(student_id=current_user.id,tutor_id=user.id).delete()
	db.session.commit()
	return redirect(url_for('home.dashboard'))

@matches.route('/message/<receiver>', methods=['POST'])
def message(receiver):
	try:
		username = current_user.username
		message = request.form.get('message')
		receiverUser = User.query.filter_by(username=receiver).first()
		new_message = Messages(username=username, sender_id=current_user.id,receiver_id=receiverUser.id, message=message)
		db.session.add(new_message)
		db.session.commit()
		#trigger event on both user channels with one call:
		#var channels = [ 'private_notifications_user1', 'private_notifications_user2'];
		#var eventData = {
		#	'channel_name': 'private-chat-user1-2',
		#	'initiated_by': 'user1'
		#	'chat_with'   : 'user2'
		#}

		pusher_client.trigger('boi', 'new-message', {'username' : username, 'message': message})
		
		return jsonify({'result' : "success"})
	except:
		return jsonify({'result' : 'failure'})
