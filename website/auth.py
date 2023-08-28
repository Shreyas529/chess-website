from flask import Blueprint,redirect,url_for,render_template,request,session,flash,get_flashed_messages,Flask
from datetime import timedelta
from .models import User
from werkzeug.security import generate_password_hash , check_password_hash
from . import db,oauth
from flask_sqlalchemy import SQLAlchemy
import time
from flask_login import login_user,login_required,logout_user,current_user
import random
from flask_mail import Mail , Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import berserk
from authlib.integrations.flask_client import OAuth
import requests
from flask import jsonify

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


def send_email(recipient_email,password):
    sender_email='chessenthusiats@gmail.com'
    sender_password="rcabavmnwsatobwd"
    subject = "Forgot Password"
    message = f"Your new password is {password}. If you want to change the password, login and reset the password"
    msg = MIMEMultipart()

    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  

    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

@auth.route("/forgot.html",methods=['POST','GET'])
def forgot():
    pwd  = str(random.randrange(10000,999999))
    if request.method == 'POST':
        email = request.form.get("email")
        if email == None:
            flash('Please Enter an Email Address',category='error')
            return redirect(url_for("auth.forgot"))
        
        else:
            #print(email)
            user = User.query.filter_by(email=email).first()
            if user == None :
                #print("\n\n\n\nUser=None\n\n\n\n")
                flash('This Email does not exist',category='error')
                return redirect(url_for('auth.forgot'))
            
            else :
                setattr(user,'password',generate_password_hash(pwd,method='sha256'))
                db.session.commit()
                send_email(email , pwd)
                flash('Email Sent Please check your inbox and spam folder',category='success')
                return redirect(url_for('auth.login'))
                # msg= Message(
                #                 f'Password Change',
                #                 sender = 'chessenthusiats@gmail.com'
                #                 recipients=[f'{email}']
                # )
                # msg.body='Hello, This email is because you forgot your password to our chess website\n This is your updated password\n{password}\n If this was not initiated by you please contact us'
                
    else :
        return render_template("forgot.html")
    
@auth.route('/lichess/login/')
def login_lichess():
    redirect_uri = url_for("auth.authorize", _external=True)
    """
    If you need to append scopes to your requests, add the `scope=...` named argument
    to the `.authorize_redirect()` method. For admissible values refer to https://lichess.org/api#section/Authentication. 
    Example with scopes for allowing the app to read the user's email address:
    `return oauth.lichess.authorize_redirect(redirect_uri, scope="email:read")`
    """
    return oauth.lichess.authorize_redirect(redirect_uri , scope="email:read")

@auth.route("/lichess/denied/")
def denied():
    return ("<h1>User denied entry</h1>")

@auth.route('/lichess/authorize/')
def authorize():
    
    if "error" in request.args and request.args["error"]=="access_denied":
        return redirect(url_for("auth.denied"))
    
    token = oauth.lichess.authorize_access_token()
    bearer = token['access_token']
    headers = {'Authorization': f'Bearer {bearer}'}

    # Add your API token to the headers
    api_token = 'lip_wq82w70I7P9jPuRoS958'
    headers['Authorization'] = f'Bearer {api_token}'
    session = berserk.TokenSession(api_token)
    client = berserk.Client(session=session)
    print(client.account.get_email())
    response = requests.get("https://lichess.org/api/account", headers=headers)
    email = client.account.get_email()
    name=response.json()['username']
    user = User.query.filter_by(email=email).first()
    password = str(random.randrange(1000000,9999999))
    
    if user:
        setattr(user,'name',name)
        setattr(user,'lichess',True)
        db.session.commit()
        return redirect(url_for('views.home'))
    
    else :
        new_user=User(email=email,name=name,password=generate_password_hash(password,method='sha256'),lichess=True)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account Created! {name}\nPassword has been sent to your email associated with lichess',category='success')
        send_email(email,password)
        user_created = User.query.filter_by(email=email).first()
        login_user(user_created,remember=True)
        return redirect(url_for('views.home'))
            
            