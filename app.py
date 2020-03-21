import os
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
bootstrap = Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


projects = open("data/github_projects.csv")
project_lines = projects.readlines()
for i in range(0, len(project_lines)):
    project_lines[i] = project_lines[i].split(",")

def register_user(username, email, password):
    accounts = open("data/accounts.csv", "a+")
    account_lines = accounts.readlines()
    for i in range(0, len(account_lines)):
        if username == account_lines[i][1] or email == account_lines[i][2]:
            return "Account not created, username or email already exists"
    id = 1000000+len(account_lines)
    line = str(id) + "," + str(username) + "," + str(email) + "," + str(password)
    account_lines.append(line)
    return "Account created"


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=50)])
    password = StringField('password', validators=[InputRequired(), Length(min=12, max=80)])
    
    def get_email(self):
        return email

    def get_username(self):
        return username
    
    def get_password(self):
        return password

class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[InputRequired(), Length(min=12, max=80)])
    remember = BooleanField("Remember me")


@app.route('/')
def default():
    return render_template("/home.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/post')
def post():
    return render_template("post.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "<h1>" + form.username.data + " " + form.password.data + "</h1>"
    return render_template("login.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        print(register_user(form.get_username, form.get_email, form.get_password))
        return "<h1>" + form.username.data + " " + form.email.data + " " + form.password.data + "</h1>"
    return render_template("signup.html", form=form)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/whoami')
def whoami():
    moi1 = "static/img/Me/moi.jpg"
    moi2 = "static/img/Me/moi2.jpg"
    moi3 = "static/img/Me/moi3.jpg"
    return render_template("whoami.html",
                           image=moi1,
                           image2=moi2,
                           image3=moi3)


@app.route('/skills')
def skills():
    return render_template("skills.html")


@app.route('/blog')
def blog():
    return render_template("blog.html")


@app.route('/projects')
def projects():
    return render_template("projects.html",
                           lines=project_lines[1:],
                           github_url="https://github.com/",
                           number=len(project_lines) - 1)


@app.route('/cv')
def cv():
    return render_template("cv.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


# app name
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", home="/home.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
