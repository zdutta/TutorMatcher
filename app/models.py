from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


class User(UserMixin,db.Model):
	"""
	Create User table
	"""
	__tablename__ = 'users'

	id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
	email = db.Column(db.String(60),index=True,unique=True)
	username = db.Column(db.String(60),index=True,unique=True)
	first_name = db.Column(db.String(60),index = True)
	last_name = db.Column(db.String(60),index = True)
	password_hash = db.Column(db.String(128))
	role = db.Column(db.String(128)) #student or tutor 
	is_admin = db.Column(db.Boolean,default=False)
	__mapper_args__ = {'polymorphic_identity':'users', 'polymorphic_on' : role}

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
		return '<User; {}'.format(self.username)


class Student(User):
	__tablename__='students'
	__mapper_args__={'polymorphic_identity':'student'}
	id = db.Column(db.Integer, db.ForeignKey('users.id'),primary_key=True)
	needs=db.Column(db.String(200))

class Tutor(User):
	__tablename__='tutors'
	__mapper_args__={'polymorphic_identity':'tutor'}
	id = db.Column(db.Integer, db.ForeignKey('users.id'),primary_key=True)
	subjects=db.Column(db.String(200))
	bio=db.Column(db.String(200))


#setting up user_loader
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))