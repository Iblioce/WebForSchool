# Adds a form, second route
from flask import Flask, render_template, request, session, redirect
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

TASK = [
      {}
]
@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
            return render_template("redPanda.html", name=session.get("name"))
    return render_template("index.html")


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
            session["username"] = request.form.get("username")
            return redirect('/')
            
    return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect('/')

"""
@app.route("/redPanda", methods=["POST"])
def redPanda():
    return render_template("redPanda.html", name=request.args.get("name"))
"""