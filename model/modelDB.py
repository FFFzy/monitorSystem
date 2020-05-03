# config=utf-8
from .DBUtil import db

class User(db.Model):

    username = db.Column(db.String(200), unique=True,primary_key = True)
    password = db.Column(db.String(50), unique=True)
    dorId = db.Column(db.String(20),unique = True)
    phonenumber = db.Column(db.String(20),unique = True)

    __tablename__ = 'user'

    def __init__(self, username=None, password=None, dorId = None, phonenumber = None):
        self.password = password
        self.username = username
        self.dorId = dorId
        self.phonenumber = phonenumber

    def __repr__(self):
        return '<User %r>' % (self.username)

class SignOn(db.Model):

    username = db.Column(db.String(200), unique=True,primary_key = True)
    password = db.Column(db.String(50), unique=True)


    __tablename__ = 'signon'

    def __init__(self, username=None, password=None):
        self.password = password
        self.username = username

    def __repr__(self):
        return '<User %r>' % (self.username)