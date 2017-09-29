from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class author_login_form(FlaskForm):
    email_address = StringField('email_address', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class author_signup_form(FlaskForm):
    email_address = StringField('email_address', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    full_name = StringField('full_name', validators=[DataRequired()])

class add_news_form(FlaskForm):
    news_title = StringField('news_title', validators=[DataRequired()])
    news_body = TextAreaField('news_body', validators=[DataRequired()])
    news_author = StringField('news_author', validators=[DataRequired()])
