from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
import website.scrape as scrape
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from website import create_app

# app.permanent_session_lifetime=timedelta(minutes=5)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app = create_app()

if __name__=="__main__":
    app.run(debug=True)



