from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    context = {
        "title": "My first page",
        "text": "Hello World!"
    }
    return render_template("index.html", **context)


@app.route("/students/")
def show_students():
    context = [
        {"f_name": "alex", "l_name": "ivanov", "age": 12, "average": 5},
        {"f_name": "peotr", "l_name": "petrov", "age": 22, "average": 15},
        {"f_name": "nikolai", "l_name": "sidorov", "age": 32, "average": 25},
        {"f_name": "ivan", "l_name": "bunin", "age": 42, "average": 35}
        ]
    return render_template("students.html", students=context)


@app.route("/news/")
def show_news():
    articles = [
        {"header": "article number one!!", "date": "12.12.23", "body": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eligendi temporibus omnis necessitatibus suscipit deserunt laborum."},
        {"header": "article number two!!", "date": "11.12.23", "body": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eligendi temporibus omnis necessitatibus suscipit deserunt laborum."},
        {"header": "article number three!!", "date": "10.12.23", "body": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eligendi temporibus omnis necessitatibus suscipit deserunt laborum."}
    ]
    return render_template("news.html", articles=articles)


@app.route("/about/")
def about():
    return "about"


@app.route("/contact/")
def contact():
    return "contact"


@app.route("/sum/<int:one> <int:two>")
def sum(one, two):
    return f"sum = {one + two}"


@app.route("/length/<length>/")
def length(length=""):
    return f"length = {len(length)}"
