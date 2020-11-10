import csv
import os

from flask import Flask, render_template,request
from model import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:anurag@localhost/lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open('curr.csv')
    reader = csv.reader(f)

    for code,country in reader:
        cur = Currency(code=code,country=country)
        db.session.add(cur)

        print('Added ',cur.country ,' having currency code ',cur.code,'.')
    db.session.commit()


if __name__=='__main__':
    with app.app_context():
        main()