from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
    name = TextField("Name", [validators.DataRequired("Please enter your name.")])
    email = TextField("Email", [validators.DataRequired("Please enter your email address.")])
    subject = TextField("Subject", [validators.DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", [validators.DataRequired("Please  enter a message.")])
    submit = SubmitField("Send")
