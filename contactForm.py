from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name", validators = [InputRequired()])
    email = StringField("Email", validators = [InputRequired(), Email()])
    message = StringField("Message", validators = [InputRequired()])