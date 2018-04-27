from flask import flash, redirect, render_template, url_for, session
from flask_login import login_required, login_user, logout_user, current_user

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
        user=Student.query.filter_by(id=current_user.id).first()
        user.needs = form.needs.data
        db.session.commit()

    elif(session['userType']=='tutor'):
        form = TutorSettingsForm()
        user=Tutor.query.filter_by(id=current_user.id).first()
        user.subjects = form.subjects.data
        user.bio = form.subjects.bio
        db.session.commit()      


    return render_template('settings/settings.html', title="Dashboard", form = form )
