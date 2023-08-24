from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
import scrape
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.secret_key = "123"
app.permanent_session_lifetime=timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __init__(self,name,email):
        self.name= name
        self.email=email
         
@app.route("/")
@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/news.html/")
def news():
    
    content=scrape.extract_news()
    safe_content=Markup(content)
    
    return render_template("news.html",context=safe_content)

@app.route("/leaderboard.html/")
def leaderboard():
    
    content = scrape.extract_players()
    safe_content= Markup(content)
    return render_template("leaderboard.html",context=content)

@app.route("/tournments.html/")
def tournments():
    
    content = scrape.extract_tournments()
    safe_content=Markup(content)
    return render_template("tournments.html",context=content)

@app.route("/rules.html/")
def rules():
    return render_template("rules.html")

@app.route("/openings.html")
def openings():
    return render_template("opening.html")

@app.route("/login/",methods=["POST","GET"])
def login():
    
    if request.method=="POST":
        session.permanent=True
        user=request.form["nm"]
        session["user"]=user
        
        found_user=users.query.filter_by(name=user).first()
        if found_user:
            session['email']=found_user.email
            
        else:
            usr=users(user,"")
            db.session.add(usr)
            db.session.commit()
            
        
        flash("Login Successful")
        return redirect(url_for("user"))

    
    else :
        #if request.method=="GET"
        if "user" in session:
            flash("Already Logged In!!")
            return redirect(url_for("user"))
        
        return render_template("login.html")
    
    
@app.route("/user/" , methods=["POST","GET"])
def user():
    email=None
    if "user" in session:
        user=session["user"]
        
        if request.method=="POST":
            email=request.form["email"]
            session["email"]=email
            found_user=users.query.filter_by(name=user).first()
            found_user.email=email
            db.session.commit()
            flash("Email was saved")
            
        else:
            if "email" in session:
                email=session["email"]
                
        return render_template("user.html",email=email)

    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/logout/")
def logout():
    
    if "user" in session:
        user=session["user"]
        flash(f"You have been logged out , {user}","info")

    session.pop("user",None)
    session.pop("email",None)
    return redirect(url_for("login"))
    

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

