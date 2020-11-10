import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Currency(db.Model):
    __tablename__ = 'currencies'
    id = db.Column(db.Integer,primary_key=True)
    code = db.Column(db.String,nullable=False)
    country = db.Column(db.String,nullable=False)

