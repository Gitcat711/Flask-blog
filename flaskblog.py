from flask import Flask, render_template

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
