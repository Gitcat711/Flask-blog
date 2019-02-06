from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '9f54c0e6d08e1103a2413087ed630d56'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file= db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='True')

    def __repr__(self):
        return f"User('{self.username}, {self.image},{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}, {self.date_posted}')"

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
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsucessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
