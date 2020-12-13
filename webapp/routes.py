from flask import render_template, url_for, flash, redirect, request, abort
from webapp import app, bcrypt
from webapp.forms import OCRForm



@app.route("/")
@app.route("/webapp")
def webapp():
    return render_template('webapp.html')


@app.route("/OCR", methods=['GET', 'POST'])
def OCR(): 
    form = OCRForm()
    if form.validate_on_submit():
        work = form.workid.data
        if form.user_token.data != app.config['SECRET']:
            return abort(404)
        else:
            return f"OCR is running on {work}"
    return render_template('OCR.html', title='OCR', form=form)

