from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    '''A class for Registration Form'''
    #our class RegistrationForm will inherit from FlaskForm in the bracket
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)]) 
    #creating a new attribute. The username in bracket will be used as our label in HTML
    #StringField means our data will be a string
    #DataRequired means the unsername cannot be empty
    #Length gives the minimum (no is 2) and Maximum (is 20 ) of what a username can be
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
                                         #the argument for the EqualTo is the field that we want the confirm pass word to be equal to
                                         #which is password in this case
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    '''A class for Login Form'''
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    remember =  BooleanField('Remember Me')                   
    submit = SubmitField('Login')
    