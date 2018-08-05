from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chores.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.available_chores import models

from application.available_chores import views

db.create_all()