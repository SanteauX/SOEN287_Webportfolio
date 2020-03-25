import os
import bcrypt
import csv
from pymongo import MongoClient
from datetime import datetime
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

########################### DATABASE
cluster = MongoClient("mongodb+srv://HugoAdmin:<yvctrd6F7GUYBVYT>@personalsite-3gjka.mongodb.net/test?retryWrites=true&w=majority")
db = cluster['Site']
collection = db['BlogPosts']

post = {"_id": 0, "author": "Hugo Joncour", "date": "25/03/2020", "Title": "test", "Subtitle": "subtitle test", "tags": ["CS", "ECON"], "body": ["part 1", "part 2"], "images": ["image 1", "image 2"]}
collection.insert_one(post)

#id, date, author, tags, title, subtitle, content
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
    author = StringField("From", validators = [InputRequired(), Length(min=1, max=80)]) 
    email = StringField("Email", validators = [InputRequired(), Email()])
    for_ = StringField("For", validators = [InputRequired(), Length(min=1, max=80)])
    title = StringField("Subject", validators = [InputRequired(), Length(min=1, max=80)])
    content = StringField("Message", validators = [InputRequired(), Length(min=1, max=800)])


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

def create_message(author, email, for_, title, content):
    print("enter messages")
    messages = open("data/messages.csv", "r+")
    message_lines = messages.readlines()
    id = 1000000+len(message_lines)
    line = str(id) + "," +str(author) + "," + str(email) + "," + str(for_) + "," + str(datetime.now()) + "," + str(title) + "," + str(content)+"\n"
    messages.write(line)
    print("write line: "+line)
    return True


def user_exists(user):
    accounts = open("data/accounts.csv", "r")
    account_lines = accounts.readlines()
    for i in range(0, len(account_lines)):
        line = account_lines[i].split(",")
        if user == line[0]:
            return True
    return False


########################### PROJECTS GITHUB
def get_github_projects():
    projects = open("data/github_projects.csv")
    project_lines = projects.readlines()
    for i in range(0, len(project_lines)):
        project_lines[i] = project_lines[i].split(",")
    return project_lines

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
        session['username'] = form.username.data
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


@app.route('/account')
@login_required
def protected():
    return render_template('protected.html')


@app.route('/myMessages', methods =['GET', 'POST'])
@login_required
def myMessages():
    lines = getMessages(session['username'])
    number = len(lines) - 1
    return render_template("myMessages.html",
                            lines = lines,
                            number = number,
                            url = "messenger.html/")

@app.route('/message')
@login_required
def message():
    return render_template("/messenge.html")


def getMessages(username):
    messages = open("data/messages.csv", "r")
    message_lines = messages.readlines()
    messages_for_me = []
    for i in range(0, len(message_lines)):
        mm = message_lines[i].split(",")
        if mm[3] == username:
            messages_for_me.append(mm)
    return messages_for_me

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
    project_lines = get_github_projects()
    return render_template("projects.html",
                           lines=project_lines[1:],
                           url="https://github.com/",
                           number=len(project_lines))


@app.route('/cv')
def cv():
    return render_template("cv.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/contactForm', methods=['GET', 'POST'])
def contactForm():
    form = ContactForm()
    if form.validate_on_submit():
        if user_exists(form.for_.data):
            print("User exists")
            message = create_message(form.author.data, form.email.data, form.for_.data, form.title.data, form.content.data)
            return render_template("formResponse.html",
                                    title="Message sent",
                                    bodyTitle="Your message was sent to "+form.for_.data,
                                    link="/contact",
                                    page="contact")
        else:
            print("User doesn't exist")
            return render_template("formResponse.html",
                                        title="Error",
                                        bodyTitle="Sorry, this user doesn't exist",
                                        link="/signup",
                                        page="registration")        
    return render_template("/contactForm.html", form=form)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", home="/home.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
