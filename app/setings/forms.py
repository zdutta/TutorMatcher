from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User,Tutor,Student

class TutorSettingsForm(FlaskForm):
    """
    Form for settings for tutors
    """
    subjects = StringField('Subject of expertise:')
    bio = StringField('Bio:')

    submit = SubmitField('Confirm')

class StudentSettingsForm(FlaskForm):
    """
    Form for settings for tutors
    """

    needs = StringField('Needs:')

    submit = SubmitField('Confirm')
