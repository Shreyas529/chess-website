from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask import Flask
from flask_mail import Mail, Message
from authlib.integrations.flask_client import OAuth

db = SQLAlchemy()
DB_NAME='database.db'

oauth = OAuth()
LICHESS_HOST = "https://lichess.org"

def create_app():
    
    app=Flask(__name__)
    app.config['SECRET_KEY']='123'
    app.permanent_session_lifetime=timedelta(minutes=5)
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['LICHESS_CLIENT_ID'] =  "lichess-oauth-flask"
    app.config['LICHESS_AUTHORIZE_URL'] = f"{LICHESS_HOST}/oauth"
    app.config['LICHESS_ACCESS_TOKEN_URL'] = f"{LICHESS_HOST}/api/token"

    oauth.__init__(app)
    oauth.register('lichess', client_kwargs={"code_challenge_method": "S256"})
    
    db.init_app(app)
    oauth.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    from .models import User
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        try:
            return User.query.get(int(id))
        except:
            pass
    
    return app

def create_database(app):
    if not path.exists('website/'+DB_NAME):
        with app.app_context():
            db.create_all()
        