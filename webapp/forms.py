from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length


class OCRForm(FlaskForm):
    workid = StringField('Work Id',
                           validators=[DataRequired(), Length(min=2, max=20)])
    user_key = PasswordField('User Key',
                        validators=[DataRequired()])
    engine_option = StringField('Engine Option', validators=[DataRequired()])
    submit = SubmitField('Run the OCR')
