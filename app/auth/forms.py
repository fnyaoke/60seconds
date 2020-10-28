#
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,ValidationError,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User

class Registration(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter yourname',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('The account exists with this email')

    def validate_username(self,data_field):
        if User.query.filter_by(username =data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = StringField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('SignIn')