from flask import flash, redirect, render_template, url_for, session
from flask_login import login_required, login_user, logout_user

from . import settings
from forms import TutorSettingsForm, StudentSettingsForm
from .. import db
from ..models import User, Tutor, Student

#for now register everyone as a student
@login_required
@settings.route('/settings', methods=['GET', 'POST'])
def settings():
    """
    Handle requests to the /register route
    Add an student to the database through the registration form
    """
    if(session['userType']=='student'):
        form = StudentSettingsForm()
    
    elif(session['userType']=='tutor'):
        form = TutorSettingsForm()

    return render_template('settings/settings.html', title="Dashboard", form = form )
