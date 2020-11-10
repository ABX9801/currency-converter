from flask import Flask,render_template,request,session
from flask_session import Session
from model import *
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:anurag@localhost/lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/',methods = ['POST','GET'])
def index():
    conv =0
    currencies = Currency.query.all()
    if request.method == 'POST':
        base = request.form.get("base")
        end  = request.form.get('end')
        amount = request.form.get('amount')

        res = requests.get('https://free.currconv.com/api/v7/convert?q='+base+'_'+end+'&compact=ultra&apiKey=4d970758dfcbc99cad7c')

        data = res.json()
        conv = float(data[base+'_'+end])*int(amount)
    return render_template('index.html',currencies = currencies,output=conv)
