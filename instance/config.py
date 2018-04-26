SECRET_KEY = 'abc1324'
#SQLALCHEMY_DATABASE_URI = 'mysql://db_admin:db2018@localhost/tutorMatcher_db'
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'tutorMatcher.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False