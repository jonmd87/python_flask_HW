from flask import Flask, url_for, request, render_template, redirect, flash, make_response
from werkzeug.utils import secure_filename
import pathlib
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route("/")
@app.route("/index/")
def index():
    response = make_response("cookie set")
    response.set_cookie("username", "admin")
    return response


@app.route("/getcookie/")
def get_cookie():
    name = request.cookies.get("username")
    return f"cookie value {name}"


@app.route("/file/<path:file>/")
def get_file(file):
    return f"your file: {escape(file)}"


@app.route("/test_url/<int:num>")
def test_url(num):
    text = f"num = {num}<br>"
    text += f"function {url_for('test_url', num=12)}<br>"
    return text


@app.route("/get/")
def get():
    if level := request.args.get("level"):
        text = f"hello old user your leve = {level}"
    else:
        text = "hello new user"
    return f"{text} \n{request.args}"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello {name}"
    return render_template("form.html")


@app.get("/submit")
def submit_get():
    return render_template("form.html")


@app.post("/submit")
def submit_post():
    name = request.form.get("name")
    return f"Hello {name}"


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        file_name = secure_filename(file.filename)
        file.save(pathlib.PurePath.joinpath(pathlib.Path.cwd(), "uploads", file_name))
        return f"file {file_name} uploaded on server"
    return render_template("upload.html")


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        "title": "page not found",
        "url": request.base_url
    }
    return render_template("404.html", **context), 404


@app.route("/redirect/")
def redirect_to_index():
    return redirect(url_for("index"))


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        flash("form sent", "success")
        return redirect(url_for("form"))
    return render_template("flash_form.html")


if __name__ == "__main__":
    app.run(debug=True)
