from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_mail import Message, Mail

login_manager = LoginManager()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
 
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'adoteumaarvoreinovasan@gmail.com'
    app.config['MAIL_PASSWORD'] = "123@Mudar"
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
  
    mail.init_app(app)
    
    from .controllers.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app