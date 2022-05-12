from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating instance of the application
app = Flask(__name__)

# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a1245ecee960ef016aa6'

# creating instance for the database
db = SQLAlchemy()

from Auth import routes
