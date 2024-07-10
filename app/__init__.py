from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) #create a flask object
app.config.from_object(Config)

#Creates an instance of the SQLAlchemy class, passing the Flask app instance to it. 
# This initializes the database connection and sets up the ORM based on the configuration settings loaded into the Flask app (e.g., SQLALCHEMY_DATABASE_URI).
db = SQLAlchemy(app) # represent the database

#Creates an instance of the Migrate class, passing the Flask app instance 
#and the SQLAlchemy instance to it. This sets up Flask-Migrate, 
# which provides database migration capabilities (e.g., creating and applying migrations).
migrate = Migrate(app, db) # represent the data migration engine

from app import routes, models # models will define the structure of the database