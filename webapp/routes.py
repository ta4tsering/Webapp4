from flask import render_template, url_for, flash, redirect
from webapp import app
from webapp.forms import RegistrationForm
from webapp.models import User, Post


posts = [
    {
        'author': 'Tashi Tsering',
        'title': 'How to use this ',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/OCR", methods=['GET', 'POST'])
def OCR():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.workid.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('OCR.html', title='OCR', form=form)


