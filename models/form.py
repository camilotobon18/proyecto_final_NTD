from wtforms import Form
from wtforms import StringField, TextField, PasswordField, IntegerField, FloatField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class LoginForm(Form):
    email = EmailField('Email',
        [
            validators.Required()
        ])
    password = PasswordField('Password',
        [
            validators.Required()
        ])
class UserForm(Form):
    name = StringField('Name', 
        [
            validators.Required(),
            validators.length(min=2, max=40, message='Enter a valid name')
        ])
    last_name = StringField('Last name',
        [   
            validators.Required(),
            validators.length(min=2, max=40, message='Enter a valid last name')
        ])
    email = EmailField('Email',
        [
            validators.Required()
        ])
    password = PasswordField('Password',
        [
            validators.Required()
        ])

class RealStateForm(Form):
    title = StringField('Title',
    [
        validators.Required(),
        validators.length(min=5, max=100, message='Enter a valid title')
    ])
    type_real_state = StringField('Type',
    [
        validators.length(min=25),
        validators.Required()
    ])
    address = StringField('Address', 
    [
        validators.Required(),
        validators.length(min=5, max=70, message='Enter a valid address')
    ])
    rooms = IntegerField('Rooms',
    [
        validators.Required()
    ])
    price = FloatField('Price',
    [
        validators.Required()
    ])
    area = IntegerField('Area',
    [
        validators.Required()
    ])
