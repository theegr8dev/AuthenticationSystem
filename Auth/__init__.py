from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating instance of the application
app = Flask(__name__)

# creating instance for the database
db = SQLAlchemy(app)

# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Auth.db'

app.config['SECRET_KEY'] = 'a1245ecee960ef016aa6'

from Auth import routes
