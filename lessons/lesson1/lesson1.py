from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<name>/")
def hello_world(name="unknown"):
    return f"Hello {name.capitalize()}"


@app.route("/file/<path:file>/")
def set_path(file):
    print(type(file))
    return f"file path {file}"


@app.route("/number/<float:num>/")
def number(num):
    return f"number = {num}"


@app.route("/html/")
def html_index():
    context = {
        "title": "html_page",
        "name": "john",
        "positive": 12
    }
    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run()
