import hashlib
from app import app, db
from flask import render_template, flash, redirect, request
from .forms import author_login_form
from .forms import author_signup_form
from .forms import add_news_form
from .models import User, News
import site_information

information = site_information.information


def get_hashed_password(user_password):
    salt = "cefalologin"
    salted_password = user_password + salt
    hashed_value = hashlib.md5(salted_password.encode())
    return hashed_value.hexdigest()


@app.route('/')
@app.route('/index')
def index():
    information["site_title"] = "Home"
    information["page_header"] = "Home"
    information["page_description"] = "Newsroom Homepage"
    return render_template(
        'home.html', information=information
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    information["site_title"] = "Login"
    information["page_header"] = "Login Page"
    information["page_description"] = "Showing Login Form"
    form = author_login_form()
    if form.validate_on_submit():
        flash('Login requested for email address="%s", password=%s' %
              (form.email_address.data, form.password.data))
        return redirect('/login')
    return render_template('login.html',
                           form=form, information=information)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    information["site_title"] = "Signup"
    information["page_header"] = "Signup Page"
    information["page_description"] = "Showing Signup Form"
    form = author_signup_form()
    if request.method == "GET":
        return render_template('signup.html',
                               form=form, information=information)
    else:
        if form.validate_on_submit():
            email_address = form.email_address.data
            password = get_hashed_password(form.password.data)
            full_name = form.full_name.data
            existing_user = User.query.filter_by(email_address=email_address).first()
            if existing_user == None:
                new_user = User(email_address=email_address, password=password, full_name=full_name)
                db.session.add(new_user)
                db.session.commit()
                flash('New user created with email address %s and the user\'s full name is %s' %
                      (email_address, full_name))
                return redirect('/')
            else:
                flash("An user existed using the " + email_address)
                return redirect('/signup')
        else:
            flash("Form validation failed")
            return redirect('/signup')


@app.route('/add_news', methods=['GET', 'POST'])
def addnews():
    information["site_title"] = "Add News"
    information["page_header"] = "Add News Page"
    information["page_description"] = "Showing Add News Form"
    form = add_news_form()

    if request.method == "GET":
        return render_template('add_news.html',
                               form=form, information=information)
    else:
        if form.validate_on_submit():
            news_title = form.news_title.data
            news_body = form.news_body.data
            news_author = form.news_author.data
            news_user_id = "1"
            new_news = News(news_title=news_title, news_body = news_body,
                            news_author = news_author, news_user_id=news_user_id)
            db.session.add(new_news)
            db.session.commit()
            flash('New news created by %s, the title is %s' %
                  (news_author, news_title))
            return redirect('/add_news')
        else:
            flash("Form validation failed")
            return redirect('/add_news')
