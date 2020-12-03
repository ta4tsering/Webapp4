from flask import render_template, url_for, flash, redirect
from webapp import app
from webapp.forms import RegistrationForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/OCR", methods=['GET', 'POST'])
def OCR():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.workid.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('OCR.html', title='OCR', form=form)


