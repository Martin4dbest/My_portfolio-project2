# Import necessary modules
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define routes for your website
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# You can add more routes for different pages

if __name__ == '__main__':
    app.run(debug=True)
