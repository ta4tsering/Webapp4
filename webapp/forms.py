from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    workid = StringField('Work id',
                           validators=[DataRequired(), Length(min=2, max=20)])
    engine_option = StringField('OCR Engine Option',
                        validators=[DataRequired()])
    engine_user = PasswordField('OCR Engine User', validators=[DataRequired()])
    submit = SubmitField('Run The OCR')
