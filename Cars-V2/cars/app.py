from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

filepath = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + filepath + '/cars.db'
db = SQLAlchemy(app)

class Cars_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer,nullable=False)
    trim = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Float, nullable=False)
