
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def default():
    return render_template("./html/index.html")

@app.route('/index')
def index():
    return render_template("./html/index.html")

@app.route('/whoami')
def whoami():
    return render_template('./HTML/template.html')

@app.route('/skills')
def skills():
    return render_template("./HTML/skills.html")

@app.route('/blog')
def blog():
    return render_template("./HTML/blog.html")

@app.route('/cv')
def cv():
    return render_template('./HTML/cv.html')

@app.route('/contact')
def contact():
    return render_template('./HTML/contact.html')

