import os
import bcrypt
import csv
from flask import Flask, session, render_template, url_for, redirect, flash, request
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


########################### CONFIG
app = Flask(__name__)
app.secret_key = os.urandom(32)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['USE_SESSION_FOR_NEXT'] = True
#SECRET_KEY = os.urandom(32)

########################### PROJECTS GITHUB
projects = open("data/github_projects.csv")
project_lines = projects.readlines()
for i in range(0, len(project_lines)):
    project_lines[i] = project_lines[i].split(",")

########################### CLASSES ###########################
class User(UserMixin):
    def __init__(self, username, email, phone, password):
        self.id = username
        self.email = email
        self.phone = phone
        self.password = password

    
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=50)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    phone = StringField('phone', validators = [InputRequired(), Length(min=6, max = 15)])
    password = StringField('password', validators=[InputRequired(), Length(min=12, max=80)])


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[InputRequired(), Length(min=12, max=80)])
    remember = BooleanField("Remember me")


class ContactForm(FlaskForm):
    name = StringField("Name", validators = [InputRequired(), Length(min=1, max=80)]) 
    email = StringField("Email", validators = [InputRequired(), Email()])
    title = StringField("Message", validators = [InputRequired(), Length(min=1, max=80)])
    message = StringField("Message", validators = [InputRequired(), Length(min=1, max=800)])


#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################

########################### FUNCTIONS ###########################

########################### USER LOADER
# this is used by flask_login to get a user object for the current user
@login_manager.user_loader
def load_user(user_id):
    user = find_user(user_id)
    if user:
        user.password = None
    return user

########################### FIND USER IN CSV
def find_user(username):
    with open('data/accounts.csv') as f:
        for user in csv.reader(f):
            if username == user[0]:
                return User(*user)
    return None

#######################################################################################################
#######################################################################################################

########################### ACCOUNT ROUTES ###########################

########################### REGISTER
@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = find_user(form.username.data)
        if not user:
            salt = bcrypt.gensalt()
            password = bcrypt.hashpw(form.password.data.encode(), salt)
            with open('data/accounts.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([form.username.data, form.email.data, form.phone.data, password.decode()])
        if not user:
            return render_template("formResponse.html",
                                    title="Signed up",
                                    bodyTitle="Welcome "+form.username.data,
                                    link="/home",
                                    page="home")
        else:
            return render_template("formResponse.html",
                                    title="Registration Error",
                                    bodyTitle="Sorry, this email or username already exists ",
                                    link="/signup",
                                    page="registration")
    return render_template("signup.html", form=form)

########################### LOG IN
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = find_user(form.username.data)
        if user and bcrypt.checkpw(form.password.data.encode(), user.password.encode()):
            login_user(user)
            return render_template("formResponse.html",
                                    title="Logged in",
                                    bodyTitle="Welcome "+form.username.data,
                                    link="/home",
                                    page="home")
        else:
            return render_template("formResponse.html",
                                    title="Login Error",
                                    bodyTitle="Wrong username or password",
                                    link="/login",
                                    page="login")
    return render_template('login.html', form=form)

########################### LOG OUT
@app.route('/logout')
@login_required
def logout():
    logout_user()
    # flash(str(session))
    return redirect('/')








#User: VYTUBNJK
#Password: ibuvyfUGYIBHJVUFGI
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################





@app.route('/')
def default():
    return render_template("/home.html")


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/post')
@login_required
def post():
    return render_template("post.html")

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

@app.route('/contactForm')
def contactForm():
    return render_template("/contactForm.html")

@app.route('/templateForm')
def templateForm():
    return render_template("/templateForm.html")

# app name
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", home="/home.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
