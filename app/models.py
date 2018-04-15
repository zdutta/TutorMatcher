from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin,db.Model):
	"""
	Create User table
	"""

	__tablename__ = 'users'

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(60),index=True,unique=True)
	username = db.Column(db.String(60),index=True,unique=True)
	first_name = db.Column(db.String(60),index = True)
	last_name = db.Column(db.Sring(60),index = True)
	password_hash db.Column(db.String(128))
	is_student = db.Column(db.Boolean)
	is_admin = db.Column(db.Boolean,default=False)

	@property
	def password(self):
		#Keep password from being accessed
		raist AttributeError('password is not a readable attribute')

	@password.setter
	def password(self,password):
		#set password to hashed password
		self.password_hash = generate_password_hash(password)

	def verify_password(self,password):
		#check if hashed password matches actual password
		return check_password_hash(self.password_hash,password)

	def __repr__(self):
		return '<User; {}'.format(self.username)

#setting up user_loader
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class Tutor(db.Model):
	"""
	Creating Tutor Table
	"""
	__tablename__='tutors'
	users = db.relationship('User',backref='tutor',lazy='dynamic')

	def __repr__(self):
		return '<Tutor: {}>'.format()

class Student(db.Model):
	"""
	Creating Student Table
	"""
	__tablename__='students'
	users = db.relationship('User',backref='student',lazy='dynamic')
