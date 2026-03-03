from . import db
from flask_login import UserMixin

class Reminder(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(30),db.ForeignKey('user.username'))
    medicine = db.Column(db.String(30),nullable = False)
    startdate = db.Column(db.Date,nullable = False)
    enddate = db.Column(db.Date,nullable = False)

    


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(30),nullable = False,unique = True)
    caretakername = db.Column(db.String(30),nullable = False)
    caretakerphone = db.Column(db.Integer,nullable = False,unique = True)
    patientname = db.Column(db.String(30),nullable = False)
    patientphone = db.Column(db.Integer,nullable = False,unique = True)
    age = db.Column(db.Integer,nullable = False)
    gender = db.Column(db.String(10),nullable = False)
    email = db.Column(db.String(30),nullable = False,unique = True)
    password = db.Column(db.String(30),nullable = False)
    reminder = db.relationship('Reminder')
