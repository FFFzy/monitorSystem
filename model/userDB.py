from model import modelDB
from .modelDB import *
def inserIntoSignOn(username,password):
    signOn = SignOn(username = username,password=password)
    db.session.add_all(signOn)
    db.session.commit()

def insertIntoUser(username,password,dorId=None,phonenumber=None):
    user = User(username = username,password= password,dorId=dorId,phonenumber=phonenumber)
    db.session.add(user)
    db.session.commit()

def getUserByuserameAndPass(username,password):
    user = User.query.filter_by(username = username,password = password).first()
    return user

def getUserByuserame(username):
    user = User.query.filter_by(username = username).first()
    return user
def updateUser(username=None,password=None,dorId=None,phonenumber=None):
    user = User.query.filter_by(username = username).first()
    user.password = password
    user.dorId = dorId
    user.phonenumber = phonenumber
    db.session.commit()
def getSignOnByNameAndPass(username,password):
    signOn = SignOn.query.filter_by(username = username,password = password).first()
    return signOn