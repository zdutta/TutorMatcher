from flask import flash, redirect, render_template, url_for, session
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import User, Tutor, Student

#for now register everyone as a student
@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an student to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        if(form.userType.data=='student'):      
            student = Student(email=form.email.data,
                                username=form.username.data,
                                first_name=form.first_name.data,
                                last_name=form.last_name.data,
                                password=form.password.data,
                                role=form.userType.data)
            db.session.add(student)
        elif(form.userType.data=='tutor'):
            tutor = Tutor(email=form.email.data,
                                username=form.username.data,
                                first_name=form.first_name.data,
                                last_name=form.last_name.data,
                                password=form.password.data,
                                role=form.userType.data)
            db.session.add(tutor) 
        db.session.commit()
        flash('You have successfully registered as a ' + form.userType.data + ' ! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an student in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        # check whether student exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            # log student in
            session['username'] = user.username
            login_user(user)
            print (session['username'])

            # redirect to the dashboard page after login
            return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')            


    # load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an student out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))