import os
from flask import render_template, url_for, flash, redirect, request, abort
from webapp import app, bcrypt
from webapp.forms import OCRForm
from webapp.utils import utility



@app.route("/")
@app.route("/webapp")
def webapp():
    return render_template('webapp.html')


@app.route("/OCR", methods=['GET', 'POST'])
def OCR(): 
    form = OCRForm()
    if form.validate_on_submit():
        OCR_engine = form.engine_choices.data
        if form.user_token.data != app.config['SECRET']:
            return abort(404)
        else:
            if form.workid.data:
                work = form.workid.data
                return f'OCR is running on {work} using engine {OCR_engine}'
            elif request.method == 'POST':
                if request.files:
                    work_file = request.files["work_file"]
                    work_file.save(os.path.join(app.config["FILES_UPLOAD"], 'file.txt'))
                    work_list = utility()
                    return f'OCR is running on engine {OCR_engine}, on work id {work_list}   '
    return render_template('OCR.html', title='OCR', form=form)