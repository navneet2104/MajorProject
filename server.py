# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:32:46 2019

@author: dell
"""

from flask import Flask, request, render_template, url_for
from sarcasm_detector import predict

app = Flask(__name__)
@app.route("/")
def first():
    return render_template('first.html')
    
@app.route("/home",methods=["GET"])
def homepage():
    return render_template('index.html')
  
@app.route("/result", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":    
        form_data = request.form
        status = predict(form_data["sentence"])
        return render_template("result.html",result=status, response=status)
    else:
        return render_template("result.html")

@app.route("/about", methods=["GET"])
def about_us():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()