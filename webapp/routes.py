import os
from flask import render_template, url_for, flash, redirect, request, abort
from webapp import app, bcrypt
from webapp.forms import OCRForm
# from werkzeug import secure_filename



@app.route("/")
@app.route("/webapp")
def webapp():
    return render_template('webapp.html')


@app.route("/OCR", methods=['GET', 'POST'])
def OCR(): 
    form = OCRForm()
    if form.validate_on_submit():
        work = form.workid.data
        OCR_engine = form.engine_choices.data
        if form.user_token.data != app.config['SECRET']:
            return abort(404)
        else:
            return f"OCR is running on {work} using engine {OCR_engine} .."
        if request.method == 'POST':
            f = request.files[f'{form.pecha_pictures.data}']
            if f.filename == '':
                flash('No selected file')
                return redirect(request.url)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f))
    return render_template('OCR.html', title='OCR', form=form)

