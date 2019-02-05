from flask import Flask, render_template, flash, redirect, url_for
from forms import RegisterationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9f54c0e6d08e1103a2413087ed630d56'

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
