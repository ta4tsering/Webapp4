from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput() 

class OCRForm(FlaskForm):
    workid = StringField('Work Id',
                           validators=[DataRequired(), Length(min=2, max=20)])
    user_key = PasswordField('User Key',
                        validators=[DataRequired()])
    engine_option = StringField('Upload Pictures', validators=[DataRequired()])
    choices = MultiCheckboxField('Engine Option', 
                        choices=[('Namsel', 'Namsel OCR Engine'),('Google', 'Google OCR Engine')]) 
    submit = SubmitField('Run the OCR')
