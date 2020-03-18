from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

moi1 = "static/img/Me/moi.jpg"
moi2 = "static/img/Me/moi2.jpg"
moi3 = "static/img/Me/moi3.jpg"

projects = open("data/github_projects.csv")
project_lines = projects.readlines()
for i in range(0, len(project_lines)):
    project_lines[i] = project_lines[i].split(",")


@app.route('/')
def default():
    return render_template("/home.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/home.html')
def home():
    return render_template("home.html")

@app.route('/whoami.html')
def whoami():
    return render_template("whoami.html",
    image=moi1,
    image2=moi2,
    image3=moi3)

@app.route('/skills.html')
def skills():
    return render_template("skills.html")

@app.route('/blog.html')
def blog():
    return render_template("blog.html")

@app.route('/projects.html')
def projects():
    return render_template("projects.html",
    lines=project_lines,
    number=len(project_lines))

@app.route('/cv.html')
def cv():
    return render_template("cv.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")





# app name 
@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html", home="/home.html") 

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)