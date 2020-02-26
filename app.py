from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def default():
    return render_template("template.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/whoami')
def whoami():
    return render_template("whoami.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/cv')
def cv():
    return render_template("cv.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
