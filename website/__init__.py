from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "voxacare"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voxacare.db'
    db.init_app(app)

    from .auth import auth
    from .reminder import reminder

    app.register_blueprint(auth,url_prefix = '/')
    app.register_blueprint(reminder,url_prefix = '/')

    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def CreateUser(id):
        return User.query.get(int(id))
    return app