from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length,ValidationError


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput() 

class OCRForm(FlaskForm):
    workid = StringField('Work Id',
                           validators=[DataRequired(), Length(min=2, max=20)])
    user_key = StringField('User Token',
                        validators=[DataRequired()])
    pecha_pictures = FileField('Upload Pictures', validators=[FileAllowed(['jpg','png'])])
    engine_choices = MultiCheckboxField('Engine Option', 
                        choices=[('Namsel', 'Namsel OCR Engine'),('Google', 'Google OCR Engine')]) 
    submit = SubmitField('Run the OCR')



    