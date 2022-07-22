
from flask import Flask
from flask import request
from flask import render_template

import joblib
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def root():
    if request.method =='POST':
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        print(r1)
        model2 = joblib.load('tree')
        r2 = model2.predict([[rates]])
        print(r2)
        return (render_template("index.html",result1=r1,result2=r2))
    else:
        return (render_template("index.html",result1="Waiting",result2="Waiting"))
app.run()
