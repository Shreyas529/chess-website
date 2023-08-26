from flask import Blueprint,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from .scrape import *
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required,current_user

views = Blueprint('views',__name__)

@views.route("/")
@views.route("/home/")
def home():
    return render_template("index.html")


@views.route("/news.html/")
@login_required
def news():
    
    content=extract_news()
    safe_content=Markup(content)
    
    return render_template("news.html",context=safe_content)


@views.route("/leaderboard.html/")
@login_required
def leaderboard():
    
    content = extract_players()
    safe_content= Markup(content)
    return render_template("leaderboard.html",context=content)


@views.route("/tournments.html/")
@login_required
def tournments():
    
    content = extract_tournments()
    safe_content=Markup(content)
    return render_template("tournments.html",context=content)


@views.route("/rules.html/")
@login_required
def rules():
    return render_template("rules.html")

@views.route("/openings.html")
@login_required
def openings():
    return render_template("opening.html")

