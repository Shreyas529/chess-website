from flask import Blueprint,redirect,url_for,render_template,request,session,flash,get_flashed_messages,Flask
from datetime import timedelta
from .models import User
from werkzeug.security import generate_password_hash , check_password_hash
from . import db
from flask_sqlalchemy import SQLAlchemy
import time
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth',__name__)

@auth.route("/login.html/",methods=['POST','GET'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password,password):
                # flash('Logged in Successfully!',category='success')
                # flash('Redirecting to Home page...',category='success')
                login_user(user,remember=True)
                for i in range(1,6):
                    #flash(f'{i}',category='success')
                    #redirect(url_for('auth.login'))
                    time.sleep(1)
                return redirect(url_for('views.home'))
            
            else:
                flash('Incorrect password, try again.',category='error')
                return redirect(url_for('auth.login'))
            
        else:
            flash('Email Does not exist.',category='error')
            return redirect(url_for('auth.login'))
    
    else :
        return render_template("/login.html")        

@auth.route("/sign-up.html/",methods=['POST','GET'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        name=request.form.get('name')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm')
        
        if len(email) < 4:
            flash('Your Email is not valid',category='error')
        elif len(name) < 2:
            flash('Enter a valid name of atleast 3 characters',category='error')
        elif password!=confirm_password:
            flash('Passwords do not match',category='error')
        elif len(password) < 7:
            flash('Password must be greater that 7 characters' , category='error')
        else:
            new_user=User(email=email,name=name,password=generate_password_hash(password,method='sha256'))
            try:
                db.session.add(new_user)
                db.session.commit()
                flash(f'Account Created! {name}',category='success')
                return redirect(url_for('auth.login'))
            
            except:
                flash(f'User with email {email} Already exists' ,category='error')
                return redirect(url_for('auth.login'))
    
    return render_template("signup.html")

@auth.route('/logout.html')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))