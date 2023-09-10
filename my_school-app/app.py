from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)

# Configure the database (SQLite in this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)


# Define the News model


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add News')


# Define routes for your website
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    news_items = News.query.all()
    return render_template('news.html', news_items=news_items)

@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        if title and content:
            new_news = News(title=title, content=content)
            db.session.add(new_news)
            db.session.commit()
            flash('News added successfully!', 'success')
            return redirect('/news')
    return render_template('add_news.html', form=form)
# You can add more routes for different pages




if __name__ == '__main__':
    app.run(debug=True)
