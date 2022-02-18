from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session

@app.route("/users/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users = users)

@app.route("/users/new")
def new_user():
    return render_template("create.html")

# relevant code snippet from server.py
@app.route('/users/new/new', methods=["POST"])
def create_friend():
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
    "first_name": request.form["first_name"],
    "last_name" : request.form["last_name"],
    "email" : request.form["email"]
    }
# We pass the data dictionary into the save method from the Friend class.
    User.save(data)
# Don't forget to redirect after saving to the database.
    return redirect('/users/')