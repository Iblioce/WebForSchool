import os

from sql import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        # Access form data
        name = request.form.get("name")
        if not name:
            return redirect("/")
        month = request.form.get("month")
        if not month:
            return redirect("/")
        try:
            month = int(month)
        except ValueError:
            return redirect("/")
        if month < 1 or month > 12:
            return redirect("/")
        day = request.form.get("day")
        if not day:
            return redirect("/")
        try:
            day = int(day)
        except ValueError:
            return redirect("/")
        if day < 1 or day > 31:
            return redirect("/")
        # Insert data into database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        return redirect("/")

    else:
        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)

@app.route("/birthdays")
def birthdays():
    birthdays_db = db.execute("SELECT * FROM birthdays")
    return jsonify(birthdays_db)

@app.route("/birthday/create", methods=["POST"])
def create_birthday():
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")
    if not name or not month or not day:
        return "Missing data", 400
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)",
    name, month, day)
    return '', 204

@app.route('/birthday/delete/<int:id>', methods=["DELETE"])
def delete_birthday(id):
    birthdays = db.execute('SELECT * FROM birthdays WHERE id = ?', id)
    if not birthdays:
        return 'Birthday not found', 404
    db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return '', 204

@app.route('/birthday/update/<int:id>', methods=["PUT"])
def update_birthday(id):
    birthdays = db.execute('SELECT * FROM birthdays WHERE id = ?', id)
    if not birthdays:
        return 'Birthday not found', 404
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")
    if not name or not month or not day:
        return "Missing data", 400
    db.execute(
    "UPDATE birthdays SET name = ?, month = ?, day = ? WHERE id = ?",
    name, month, day, id,
    )
    return '', 204