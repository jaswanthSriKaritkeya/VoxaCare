from flask import Blueprint,render_template,redirect,request,flash,url_for
from flask_login import login_required,login_user,logout_user,current_user
from .models import User,Reminder
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
auth = Blueprint('auth',__name__)

@auth.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        check = User.query.filter_by(email = email).first()
        if check:
            if check_password_hash(check.password,password):
                flash("Logined successful ",category='success')
                login_user(check,remember=True)
                return redirect('/')
            else:
                flash("Password not Matched",category='error')
            # else:
            #     flash("Password has not Matched with Confirm Password",category='error')
        else:
            flash("Account have not Existed",category='error')
    return render_template('login.html',user = current_user)
    

@auth.route('/signin',methods = ['GET','POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        caretakername = request.form.get('caretakername')
        caretakerphone = request.form.get('caretakerphone')
        patientname = request.form.get('patientname')
        patientphone = request.form.get('patientphone')
        age = request.form.get('age')
        gender = request.form.get('gender')
        email = request.form.get("email")
        password = request.form.get('password')
        conpassword = request.form.get('ConPassword')
        check = User.query.filter_by(email = email).first()
        if check:
            flash("Account alredy exist",category='error')
            return redirect('/login')
        elif(password != conpassword):
            flash("Password Incorrect",category = 'error')
        elif(len(password) < 8):
            flash("Password length is less then 8 Character",category ='error')
        else:
            newuser = User(username = username,caretakername = caretakername,caretakerphone = caretakerphone,patientname = patientname,patientphone = patientphone,age = age,gender = gender,email = email,password = generate_password_hash(password))
            db.session.add(newuser)
            db.session.commit()
            flash("Account created Successfully",category= 'success')
            login_user(newuser,remember=True)
            return redirect('/')
    return render_template('signin.html',user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))