from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    first_name= StringField('First Name', validators=[DataRequired()])
    last_name= StringField('Last Name')
    email= StringField('Email', validators=[DataRequired(), Email()])
    country= StringField('Country')
    subject= StringField('Subject')
    message= TextAreaField('Message', validators=[DataRequired()])

