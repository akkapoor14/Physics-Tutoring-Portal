# this is a file containing our datamodels

from app import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column('id',db.Integer,primary_key=True)

    netid = db.Column('netid',db.String(50),unique=True,nullable=False)
    name = db.Column('name',db.String(100),nullable=False)
    email = db.Column('email',db.String(50),unique=True,nullable=False)
    bio = db.Column('bio',db.String(500),nullable=True)

    isStudent = db.Column('is_student',db.Boolean,default=True)
    isTutor = db.Column('is_tutor',db.Boolean,default=False)
    isAdmin = db.Column('is_admin',db.Boolean,default=False)


    def __init__(self, netid, name, email):
        self.netid = netid
        self.name = name
        self.email = email


    def __repr__(self):
        return '<id {}>'.format(self.id)
