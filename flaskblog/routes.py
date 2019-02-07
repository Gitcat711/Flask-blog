from flask import render_template, flash, redirect, url_for
from flaskblog.forms import RegisterationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app, db , bcrypt
from flask_login import login_user, current_user, logout_user

posts = [
 {
 'name': 'Sergio Aguero',
 'title': 'Stiker',
 'content': 'This is my poor performance in UEFA',
 'date_posted': 'April 10 2019'
 },
 {
 'name': 'David Silva',
 'title': 'Winning is our Hobby',
 'content': 'A Midfielder in a making news with overconfidence with citys win',
 'date_posted': 'April 09 2019'
 }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user= User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful, check email or password', 'danger')

    return render_template('login.html', title='login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))