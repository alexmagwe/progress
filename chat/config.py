import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Development:
    DB_NAME='progress'
    SECRET_KEY='7ca1b230ca5bcda875a3c5a1eb2babc20233226775f7619c904e8902a3a36e22'
    SQLALCHEMY_DATABASE_URI='sqlite:////'+os.path.join(basedir,DB_NAME)+'.sqlite'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    FLASK_APP='app.py'

configs={'development':Development}
	
