from flask import Flask # Importing the Flask class from flask framework
from flask_sqlalchemy import SQLAlchemy # Importing the SQL database from the sqlalchemy package
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from flask_migrate import Migrate

app = Flask(__name__) # Setting the name of the current flask module to an instance of the Flask class (Instantiate a flask application)

app.config['SECRET_KEY'] = '2f1383c15f278ee889b357169d63c4aa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///greenmile.db'
db = SQLAlchemy(app) # the sqlalchemy instant
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from green import routes # importing our routes 

