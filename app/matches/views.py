from flask import render_template
from flask_login import login_required #might not be required

from . import matches

@matches.route('/messages')
@login_required
def messages():
	return render_template('matches/messages.html', title="Messages")