from flask import Flask, render_template, url_for

app = Flask(__name__)

moi1="https://scontent.fymq2-1.fna.fbcdn.net/v/t1.0-9/84984305_482770935946978_1289698118287228928_n.jpg?_nc_cat=106&_nc_sid=85a577&_nc_ohc=DdlM5FXPQowAX-WRLwk&_nc_ht=scontent.fymq2-1.fna&oh=c1ed3da00a2a393ebf1767707e2e465d&oe=5EF2255F"
moi2="https://scontent.fymq2-1.fna.fbcdn.net/v/t1.0-9/75307991_403491640541575_3558420597039955968_n.jpg?_nc_cat=109&_nc_sid=7aed08&_nc_ohc=FPILblfz9MgAX9fN41u&_nc_ht=scontent.fymq2-1.fna&oh=1e830374d29b1101e365e75d25881730&oe=5EF3F6F1"
@app.route('/')
def default():
    return render_template("template.html")

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
    image2=moi2)

@app.route('/skills.html')
def skills():
    return render_template("skills.html")

@app.route('/blog.html')
def blog():
    return render_template("blog.html")

@app.route('/projects.html')
def projects():
    return render_template("projects.html")

@app.route('/cv.html')
def cv():
    return render_template("cv.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
