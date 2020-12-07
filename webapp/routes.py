from flask import render_template, url_for, flash, redirect
from webapp import app
from webapp.forms import OCRForm

user_key = "tashi123"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/OCR" )
def OCR():
    form = OCRForm()
    return render_template('OCR.html', title='OCR', form=form)

