from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://blog:blog123@localhost/posts'
db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(50))
    subtitle= db.Column(db.String(50))
    author= db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
    
    def __init__(self, title, subtitle, author, date_posted, content):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date_posted = date_posted
        self.content = content


@app.route('/')
def index():
    #gettig all from the database
    #posts = Blogpost.query.all()
    #here we want to post the date in order by date
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    #date_posted = post.date_posted.strftime('%B %d, %Y')

    return render_template('post.html', post=post,)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/addpost', methods=['POST'])
def addpost():
    #getting the information
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
    
    #Saving them to database
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))
if __name__ == '__main__:':
    blog.run(debug=True)
