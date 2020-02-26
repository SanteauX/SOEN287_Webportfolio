from flask import Flask, render_template

app = Flask(__name__, template_folder="../html")


@app.route('/')
def default():
    return render_template("index.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/whoami')
def whoami():
    loremIpsum = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
                 "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type " \
                 "and scrambled it to make a type specimen book. It has survived not only five centuries, " \
                 "but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised " \
                 "in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently " \
                 "with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. "

    list = [loremIpsum, loremIpsum, loremIpsum, loremIpsum]

    return render_template("template.html", list = list)


@app.route('/contact')
def contact():

    return render_template("template.html")


@app.route('/skills')
def skills():
    return render_template("template.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
