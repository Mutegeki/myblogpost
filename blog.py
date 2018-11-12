from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://post:post123@localhost/blog'
db = SQLAlchemy(blog)

class Person(db.Model):
    id = db.Column(db.integer, primary_key=True)
    fisrtName = db.Column(db.string(120), unique=False)

    def __init__(self, fisrtName):
        self.fisrtName = fisrtName

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == '__main__:':
    db.create_all()
    blog.run(debug=True)
