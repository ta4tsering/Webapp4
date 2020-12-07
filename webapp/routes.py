from flask import render_template, url_for, flash, redirect, request
from webapp import app
from webapp.forms import OCRForm

user_key = "tashi123"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/OCR", methods=['GET', 'POST'])
def OCR(): 
    form = OCRForm()
    if request.method == 'POST' :
        request.form.get("choices")
    return render_template('OCR.html', title='OCR', form=form)

