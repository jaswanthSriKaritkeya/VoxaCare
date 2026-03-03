from flask import Blueprint,render_template
from .auth import current_user
reminder = Blueprint('reminder',__name__)
@reminder.route('/')
def index():
    return render_template('index.html',user = current_user)
@reminder.route('/home')
def home():
    return render_template('index.html',user = current_user)
@reminder.route('/reminder',methods = ['GET','POST'])
def reminders():
    return render_template('reminder.html',user = current_user)
@reminder.route('/dummy')
def dummy():
    return render_template('dummy.html')