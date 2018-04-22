from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class Tutor(UserMixin,db.Model):
	"""
	Create User table
	"""
	__tablename__ = 'tutors'

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(60),index=True,unique=True)
	username = db.Column(db.String(60),index=True,unique=True)
	first_name = db.Column(db.String(60),index = True)
	last_name = db.Column(db.String(60),index = True)
	password_hash = db.Column(db.String(128))
	is_admin = db.Column(db.Boolean,default=False)

	@property
	def password(self):
		#Keep password from being accessed
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self,password):
		#set password to hashed password
		self.password_hash = generate_password_hash(password)

	def verify_password(self,password):
		#check if hashed password matches actual password
		return check_password_hash(self.password_hash,password)

	def __repr__(self):
		return '<Tutor; {}'.format(self.username)

class Student(UserMixin,db.Model):
	"""
	Create User table
	"""
	__tablename__ = 'students'

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(60),index=True,unique=True)
	username = db.Column(db.String(60),index=True,unique=True)
	first_name = db.Column(db.String(60),index = True)
	last_name = db.Column(db.String(60),index = True)
	password_hash = db.Column(db.String(128))
	is_admin = db.Column(db.Boolean,default=False)

	@property
	def password(self):
		#Keep password from being accessed
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self,password):
		#set password to hashed password
		self.password_hash = generate_password_hash(password)

	def verify_password(self,password):
		#check if hashed password matches actual password
		return check_password_hash(self.password_hash,password)

	def __repr__(self):
		return '<Student; {}'.format(self.username)

#setting up user_loader
@login_manager.user_loader
#def load_user(user_id,user_type):
def load_user(user_id):
	user_type='student'
	#make sure to delete this statement later
	if(user_type == 'tutor'):
		return Tutor.query.get(int(user_id))
	elif(user_type=='student'):
		return Student.query.get(int(user_id))
	#return User.query.get(int(user_id))

