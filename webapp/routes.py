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
        work = form.workid.data
        OCR_engine = form.engine_choices.data
        if form.user_token.data != app.config['SECRET']:
            return abort(404)
        elif request.method == 'POST':
            if request.files:
                work_file = request.files["work_file"]
                work_file.save(os.path.join(app.config["FILES_UPLOAD"], work_file.filename))
                return f'OCR is running on {work} using engine {OCR_engine}'
            utility()
        return f'OCR is running on {work} using engine {OCR_engine}'
    return render_template('OCR.html', title='OCR', form=form)
    #     else:
    #         return f"OCR is running on {work} using engine {OCR_engine} .."
    #     if request.method == 'POST':
    #         infile = form.work_file.data
    #         if infile.filename == '':
    #             flash('No selected file')
    #             return redirect(request.url)
    #         file_content = utility(infile)
    #     return f'the work id { file_content}'
    # return render_template('OCR.html', title='OCR', form=form)


