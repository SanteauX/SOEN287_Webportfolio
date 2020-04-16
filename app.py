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

########################### DATE
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
weekday = now.today().strftime('%A')

#######################################################################################################
#######################################################################################################

########################### CLASSES ###########################
class User(UserMixin):
    def __init__(self, username, email, phone, password):
        self.id = username
        self.email = email
        self.phone = phone
        self.password = password

    def get_username(self):
        return self.username
    
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=50)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    phone = StringField('phone', validators = [InputRequired(), Length(min=6, max = 15)])
    password = StringField('password', validators=[InputRequired(), Length(min=12, max=80)])


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[InputRequired(), Length(min=12, max=80)])

class ContactForm(FlaskForm):
    author = StringField("From", validators = [InputRequired(), Length(min=1, max=80)]) 
    email = StringField("Email", validators = [InputRequired(), Email()])
    for_ = StringField("For", validators = [InputRequired(), Length(min=1, max=80)])
    title = StringField("Subject", validators = [InputRequired(), Length(min=1, max=80)])
    content = StringField("Message", validators = [InputRequired(), Length(min=1, max=800)])

class PostForm(FlaskForm):
    bloggername = StringField("Bloggername", validators = [InputRequired(), Length(min=1, max=80)])
    title = StringField("Title", validators = [InputRequired(), Length(min=1, max=80)])
    content = StringField("Content", validators = [InputRequired(), Length(min=1, max=800000)])

class resetPasswordForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    phone = StringField('Phone', validators = [InputRequired(), Length(min=6, max = 15)])
    password = StringField('New password', validators=[InputRequired(), Length(min=12, max=80)])
    passwordConfirmation = StringField('Password Confirmation', validators=[InputRequired(), Length(min=12, max=80)])

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
                return User(*user[0:4])
    return None

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

########################### FIX DATE PROJECT GITHUB
def remove_time(time):
    string = ""
    for i in range(0, len(time)):
        if(time[i] == "T"):
            return string
        elif(time[i] == "-"):
            string+= "/"
        else:
            string+=time[i]
    return string


########################### STATISTICS
def connection(username):
    connections = open("data/connections.csv", "a+")
    line = str(day) + "," + str(month) + "," + str(year) + "," + str(weekday) + "," + str(hour) + "," + username + "\n"
    connections.write(line)
    print("write line: "+line)
    return True

def how_many_users():
    users = open("data/accounts.csv")
    user_lines = users.readlines()
    return len(user_lines)-1

def how_many_messages():
    messages = open("data/messages.csv")
    message_lines = messages.readlines()
    return len(message_lines)-1

def how_many_connections():
    connections = open("data/connections.csv")
    connection_line = connections.readlines()
    return len(connection_line)-1

def get_data_connections_hours():
    connections = open("data/chartjs.csv")
    connections_hours = connections.readlines()
    c = connections_hours[1].split(",")
    for i in range(0, len(c)):
        c[i] = int(c[i])
    print(c)
    return c

def how_many_blog_articles():
    blog_articles = open("data/blog_posts.csv")
    blog_article_lines = blog_articles.readlines()
    return len(blog_article_lines)-1

def create_message(author, email, for_, title, content):
    print("enter messages")
    messages = open("data/messages.csv", "r+")
    message_lines = messages.readlines()
    id = 1000000+len(message_lines)
    line = str(id) + "," +str(author) + "," + str(email) + "," + str(for_) + "," + str(datetime.now()) + "," + str(title) + "," + str(content)+"\n"
    messages.write(line)
    print("write line: "+line)
    return True

######################### CREATE A BLOG ARTICLE
def create_blog_post(author, day, month, year, title, content):
    print("create blog post")
    posts = open("data/blog_posts.csv", "r+")
    post_lines = posts.readlines()
    id = 1000000+len(post_lines)
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    line = str(id) + "," +str(author) + "," + str(day) + "," + str(month) + "," + str(year) + "," + str(title) + "," + str(content)+"\n"
    print("write line: "+line)
    posts.write(line)
    return True

######################### CREATE 2D CHART MATRIX
def connection_chart1():
    ocsv = open("data/connections.csv", "r")
    ncsv = open("data/chartjs.csv", "w")
    ocsv_lines = ocsv.readlines()
    line = "0"
    for i in range(1, 24):
        line+= ","+str(i)
    ncsv.write(line+"\n")
    line2 = line.split(",")
    for i in range(0, len(line2)):
        line2[i] = 0
    for i in range(1, len(ocsv_lines)):
        ocsv_line = ocsv_lines[i].split(",")
        z = int(ocsv_line[4])
        line2[z]+=1
    csv2 = str(line2[0])
    for i in range(1, len(line2)):
        csv2+= ","+str(line2[i])
    ncsv.write(csv2)

def connection_chart2():
    ocsv = open("data/connections.csv", "r")
    ncsv = open("data/chartjs2.csv", "w")
    days = "Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday"
    ncsv.write(days)
    dayz = days.split(",")
    lines = ocsv.readlines()
    line2 = dayz
    for i in range(0, len(line2)):
        line2[i] = 0
    dayz = days.split(",")
    for i in range(0, len(lines)):
        line = lines[i].split(",")
        z = line[3]
        for j in range(0, len(dayz)):
            if z == dayz[j]:
                line2[j]+=1
    print(dayz)
    print(line2)

######################### CHANGE PASSWORD/FORTGOT PASSWORD
def change_password(username, email, phone, password, passwordConfirmation):
    accounts = open("data/accounts.csv", "r+")
    account_lines = accounts.readlines()
    for i in range(1, len(account_lines)):
        line = account_lines[i].split(",")
        print(line[0]+ " ==  " + username + " & "+ line[1] +" == "+ email+" & "+ line[2]+" == "+phone)
        if(line[0] == username and line[1] == email and line[2] == phone and password == passwordConfirmation):
            change_password_changeline(username, email, phone, password, line[4], line[5], line[6])
            return True
    return False

def change_password_changeline(username, email, phone, password, day, month, year):
    salt = bcrypt.gensalt()
    newpassword = bcrypt.hashpw(password.encode(), salt)
    line = username+","+email+","+str(phone)+","+newpassword.decode()+","+str(day)+","+str(month)+","+str(year)
    accounts = []
    a = open("data/accounts.csv", "r")
    lines = a.readlines()
    for i in range(0, len(lines)):
        x = lines[i].split(",")
        if (x[0] != username):
            accounts.append(lines[i])
    accounts.append(line)
    print(accounts)
    a.close()
    a = open("data/accounts.csv", "w")
    for i in range(0, len(accounts)):
        a.write(accounts[i])
    a.close()

######################### FIND & RETURN EMSSAGE
def return_message(id):
    messages = open("data/messages.csv")
    message_lines = messages.readlines()
    for i in range(1, len(message_lines)):
        line = message_lines[i].split(",")
        if str(line[0]) == str(id):
            return message_lines[i]
    return False

######################### FIND & RETURN MESSAGE
def return_article(id):
    articles = open("data/blog_posts.csv")
    article_lines = articles.readlines()
    for i in range(1, len(article_lines)):
        line = article_lines[i].split(",")
        if str(line[0]) == str(id):
                return article_lines[i]
    return False

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
                writer.writerow([form.username.data, form.email.data, form.phone.data, password.decode(), day, month, year])
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
            connection(form.username.data)
            return redirect('/account')
            # return render_template("formResponse.html",
            #                         title="Logged in",
            #                         bodyTitle="Welcome "+form.username.data,
            #                         link="/home",
            #                         page="home")
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

########################### RESET PASSWORD
@app.route('/forgotPasswordForm', methods=['GET', 'POST'])
def forgotPassword():
    form = resetPasswordForm()
    if form.validate_on_submit():
        if change_password(form.username.data, form.email.data, form.phone.data, form.password.data, form.passwordConfirmation.data):
            return render_template("formResponse.html",
                            title="Reset password",
                            bodyTitle="Your password was reseted ",
                            link="/login",
                            page="login")
        else:
            return render_template("formResponse.html",
                            title="Reset password",
                            bodyTitle="Your identity couldn't be confirmed, we can't reset the password ",
                            link="/login",
                            page="login")
    return render_template("forgotPasswordForm.html", form=form)

########################### STATISTICS
@app.route('/statistics')
@login_required
def statistics():
    connection_chart1()
    connection_chart2()
    users = how_many_users()
    messages = how_many_messages()
    connections = how_many_connections()
    data_hours = get_data_connections_hours()
    blog_articles = how_many_blog_articles()
    data = open("data/connections.csv", "r").readlines()
    return render_template('statistics.html', 
                            connections = connections,
                            accounts = users,
                            messages = messages,
                            blog = blog_articles,
                            data = data[1],
                            chartData = connection_chart2,
                            listhours = data_hours)

########################### CREATE A BLOG ARTICLE
@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        create_blog_post(form.bloggername.data, datetime.day, datetime.month, datetime.year, form.title.data, form.content.data)
        return render_template("formResponse.html",
                            title="Blog article posted",
                            bodyTitle="Your blog article was posted ",
                            link="/blog",
                            page="blog")
    return render_template("/post.html", form=form)

########################### ACCOUNT
@app.route('/account')
@login_required
def account():
    return render_template('account.html')

########################### MESSAGES
@app.route('/myMessages', methods =['GET', 'POST'])
@login_required
def myMessages():
    lines = getMessages(session['username'])
    number = len(lines)
    return render_template("myMessages.html",
                            lines = lines,
                            number = number,
                            url = "messenger/")

########################### MESSAGE
@app.route('/messenger/<messageID>', methods =['GET', 'POST'])
@login_required
def messenger(messageID):
    message = return_message(messageID).split(",")
    print(message)
    return render_template("messenger.html", message=message)

########################### BLOG
def return_blog(id):
    blog = open("data/blog_posts.csv")
    blog_lines = blog.readlines()
    for i in range(1, len(blog_lines)):
        line = blog_lines[i].split(",")
        #print(line)
        return line
    return False

def get_blogs():
    blog = open("data/blog_posts.csv")
    blog_lines = blog.readlines()
    for i in range(1, len(blog_lines)):
        line = blog_lines[i].split(",")
        line[2] = str(line[2])+"/"+str(line[3])+"/"+str(line[4])
        line.pop(3)
        line.pop(3)
        line = line[0]+","+line[1]+","+line[2]+","+line[3]
        blog_lines[i] = line.split(",")
    return blog_lines

@app.route('/article/<articleID>')
def blog_article(articleID):
    article = return_article(articleID).split(",")
    #print(article)
    return render_template("article.html/", article=article)


########################### MESSAGE SOMEBODY
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

######################### GET MESSAGES SENT AT YOUR ACCOUNT
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

######################### ROUTES

@app.route('/')
def default():
    return render_template("/home.html")

@app.route('/index')
def index():
    return render_template("index.html")

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
    blog_lines = get_blogs()
    #for i in range(0, len(blog_lines)):
        #print(blog_lines[i])
    return render_template("blog.html",
                            lines=blog_lines[1:],
                            url = "/article/",
                            number=len(blog_lines)-1)

@app.route('/projects')
def projects():
    #if myProjects.scrapeMyProjects():
    project_lines = get_github_projects()
    for i in range(0, len(project_lines)):
        project_lines[i][3] = remove_time(project_lines[i][3])
        print(project_lines[i])
    return render_template("projects.html",
                        lines=project_lines[1:],
                        url="https://github.com/",
                        number=len(project_lines))
    #else:
    #    print("Big Problem")

@app.route('/cv')
def cv():
    return render_template("cv.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

######################### ERROR 404
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", home="/home.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
