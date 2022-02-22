from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session

@app.route("/users/")
def index():

    users = User.get_all()
    print(users)
    return render_template("read_all.html", users = users)

@app.route("/users/new")
def new_user():
    return render_template("create.html")


@app.route('/users/new/new', methods=["POST"])
def create_friend():


    data = {
    "first_name": request.form["first_name"],
    "last_name" : request.form["last_name"],
    "email" : request.form["email"]
    }

    User.save(data)

    return redirect('/users/')

@app.route('/user/<int:id>/')
def show_user(id):
    user = User.get_one({'id': id})
    return render_template("show_user.html", user=user)

@app.route('/user/<int:id>/edit')
def edit_user(id):
    user = User.get_one({'id':id})
    return render_template('edit_user.html', user=user)

@app.route('/users/<int:id>/update', methods=["POST"])
def update_user(id):
    User.update_one(request.form)
    return redirect('/users/')